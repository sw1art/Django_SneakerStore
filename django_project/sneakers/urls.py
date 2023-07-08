from django.urls import path

from .views import SneakerListView, SneakerDetailView, SearchResultsListView

urlpatterns = [
    path('', SneakerListView.as_view(), name='sneaker_list'),
    path('<slug:slug>-<uuid:uuid>/', SneakerDetailView.as_view(), name='sneaker_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]

