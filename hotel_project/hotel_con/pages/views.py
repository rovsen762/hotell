from django.shortcuts import render
from django.views.generic import TemplateView
from hotels.models import Hotel
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
    model = Hotel
    content_object_name = 'hotels'
    pagine_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotels'] = Hotel.objects.all().order_by('-created_date')[:3]
        return context