from django.shortcuts import render, redirect, get_object_or_404
from hotels.models import Hotel, Variation
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View



def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

@login_required(login_url='login')
def add_to_cart(request, hotel_id):
    current_user = request.user
    hotel = Hotel.objects.get(id=hotel_id)
    if current_user.is_authenticated:
        hotel_variation = []
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]

                try:
                    variation = Variation.objects.get(hotel=hotel, variation_category__iexact=key, variation_value__iexact=value)
                    hotel_variation.append(variation)
                except:
                    pass


        is_cart_item_exists = CartItem.objects.filter(hotel = hotel, user=current_user).exists()
        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(hotel=hotel, user=current_user)
            ex_var_list = []
            id = []
            for item in cart_item:
                existing_variation = item.variations.all()
                ex_var_list.append(list(existing_variation))
                id.append(item.id)

            if hotel_variation in ex_var_list:
                # increase the cart item quantity
                index = ex_var_list.index(hotel_variation)
                item_id = id[index]
                item = CartItem.objects.get(hotel=hotel, id=item_id)
                item.quantity += 1
                item.save()

            else:
                item = CartItem.objects.create(hotel=hotel, quantity=1, user=current_user)
                if len(hotel_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*hotel_variation)
                item.save()
        else:
            cart_item = CartItem.objects.create(
                hotel=hotel,
                quantity = 1,
                user = current_user,
            )
            if len(hotel_variation) > 0:
                cart_item.variations.clear()
                cart_item.variations.add(*hotel_variation)
            cart_item.save()
        return redirect('cart')
    
def cart(request,cart_items=None):
    try:
        
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        
    except ObjectDoesNotExist:
        pass #just ignore

    context = {
        'cart_items': cart_items,
    }
    return render(request, 'cart.html', context)


def remove_cart_item(request, hotel_id, cart_item_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(hotel=hotel, user=request.user, id=cart_item_id)
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(hotel=hotel, cart=cart, id=cart_item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

