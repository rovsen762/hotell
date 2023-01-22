from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customer(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'