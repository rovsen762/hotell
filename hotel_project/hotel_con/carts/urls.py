from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<int:hotel_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_cart_item/<int:hotel_id>/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item'),
]
