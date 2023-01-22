from django.db import models
from accounts.models import Customer
from hotels.models import Hotel, Variation

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    person_number = models.IntegerField()
    order_begin_date = models.DateField()
    order_end_date = models.DateField()
    order_note = models.TextField()
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name


class OrderHotel(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.hotel.name