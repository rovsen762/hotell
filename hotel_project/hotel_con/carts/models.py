from django.db import models
from accounts.models import Customer
from hotels.models import Hotel,Variation

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    cart    = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.hotel.name