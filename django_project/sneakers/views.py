from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from .models import Sneaker
from elasticsearch_dsl import Search, Q

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
        if query:
            # Разбиваем запрос на отдельные слова
            query_words = query.split()
            # Создаем поиск Elasticsearch для выполнения фразового поиска для каждого слова
            search = Search(index='sneakers')
            for word in query_words:
                search = search.query('match_phrase', title=word)
            # Комбинируем поисковые запросы с помощью оператора "must" (или "and")
            search = search.query('bool', must=[Q('match_phrase', title=word) for word in query_words])
            # Получаем результаты поиска
            response = search.execute()
            hits = response.hits
            # Извлекаем список идентификаторов найденных объектов
            sneaker_ids = [hit.meta.id for hit in hits]
            # Возвращаем объекты модели Sneaker, отсортированные по порядку их появления в результате поиска
            return Sneaker.objects.filter(id__in=sneaker_ids).order_by('-id')
        return Sneaker.objects.none()