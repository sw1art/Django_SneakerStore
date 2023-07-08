from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q

from accounts.models import CustomUser
from .models import Sneaker

class SneakerListView(LoginRequiredMixin, ListView):
    model = Sneaker
    template_name = 'sneakers/sneaker_list.html'
    context_object_name = 'sneaker_list'
    login_url = 'account_login'

class SneakerDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Sneaker
    template_name = 'sneakers/sneaker_detail.html'
    context_object_name = 'sneaker_detail'
    slug_url_kwarg = 'slug'
    login_url = 'account_login'
    permission_required = 'sneakers.base_status'
    queryset = Sneaker.objects.all().prefetch_related('reviews__author',)


class SearchResultsListView(ListView):
    model = Sneaker
    template_name = 'sneakers/search_results.html'
    context_object_name = 'sneaker_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Sneaker.objects.filter(Q(title__icontains=query))

