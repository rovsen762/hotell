
from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from carts.models import CartItem
from .models import Order, OrderHotel
from .forms import OrderForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin





class PlaceOrder(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        form = OrderForm()
        context = {
            'form': form
        }

        return render(self.request, 'place_order.html', context)

    def post(self, *args, **kwargs):
        form = OrderForm(self.request.POST or None)
        
        try:
            
            cart_items = CartItem.objects.filter(user=self.request.user)
            
            if form.is_valid():
                data = Order()
                data.first_name = form.cleaned_data['first_name']
                data.last_name = form.cleaned_data['last_name']
                data.phone = form.cleaned_data['phone']
                data.email = form.cleaned_data['email']
                data.person_number = form.cleaned_data['person_number']
                data.order_begin_date = form.cleaned_data['order_begin_date']
                data.order_end_date = form.cleaned_data['order_end_date']
                data.order_note = form.cleaned_data['order_note']
                data.user = self.request.user
                data.save()

                for item in cart_items:
                    order_hotel = OrderHotel()
                    order_hotel.order = data
                    order_hotel.user = item.user
                    order_hotel.hotel = item.hotel
                    order_hotel.save()

                    cart_items = CartItem.objects.get(id=item.id)
                    hotel_variation = cart_items.variations.all()
                    order_hotel = OrderHotel.objects.get(id=order_hotel.id)
                    order_hotel.variations.set(hotel_variation)
                    order_hotel.save()

                #CartItem.objects.filter(user=self.request.user).delete()

                messages.success(self.request, 'Your order has been placed successfully')
                return redirect('place_order')

        except ObjectDoesNotExist:
            messages.error(self.request, 'You do not have an active order')
            return redirect('place_order')





