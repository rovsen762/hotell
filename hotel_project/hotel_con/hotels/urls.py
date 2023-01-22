from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotels, name='hotels'),
    path('<int:hotel_id>', views.hotel_detail, name='hotel_detail'),
]
