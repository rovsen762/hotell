from django.urls import path
from . import views
from pages.views import IndexView

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]