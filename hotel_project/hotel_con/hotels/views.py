from django.shortcuts import render
from .models import Hotel, Variation, HotelGallery
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages


# Create your views here.

def hotels(request):
    hotels = Hotel.objects.all()
    context = {
        'hotels': hotels
    }
    return render(request, 'hotels.html', context)

def hotel_detail(request,hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    hotel_gallery = HotelGallery.objects.filter(hotel_id = hotel.id)
    variations = Variation.objects.filter(hotel=hotel)
    context = {
        'hotel': hotel,
        'hotel_gallery': hotel_gallery,
        'variations': variations
    }
    return render(request, 'hotel_detail.html', context)


