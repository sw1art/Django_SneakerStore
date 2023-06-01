from django.views.generic import ListView, DetailView

from .models import Sneaker

class SneakerListView(ListView):
    model = Sneaker
    template_name = 'sneakers/sneaker_list.html'
    context_object_name = 'sneaker_list'

class SneakerDetailView(DetailView):
    model = Sneaker
    template_name = 'sneakers/sneaker_detail.html'
    context_object_name = 'sneaker_detail'
    slug_url_kwarg = 'slug'