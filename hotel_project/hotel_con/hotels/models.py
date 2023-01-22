from django.db import models
from django.urls import reverse
from accounts.models import Customer
# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    images = models.ImageField(upload_to='photos/hotels')
    description = models.TextField()
    price = models.IntegerField()
    created_date  = models.DateTimeField(auto_now_add=True)

    def get_url(self):
        return reverse('hotel_detail', args=[self.slug])

    def __str__(self):
        return self.name

    def get_add_to_cart_url(self):
        return reverse('add_to_cart', kwargs={ 'slug': self.slug })
    
class VariationManager(models.Manager):

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)

variation_category_choice = (
    ('size', 'size'),
)

class Variation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date  = models.DateTimeField(auto_now_add=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value

class HotelGallery(models.Model):
    hotel = models.ForeignKey(Hotel, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/hotels')

    def __str__(self):
        return self.hotel.name

    class Meta:
        verbose_name = 'hotelgalley'
        verbose_name_plural = 'hotel gallery'

