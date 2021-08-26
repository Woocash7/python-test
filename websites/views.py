from django.db.models import query
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from websites.models import Website, WebPage, WebsiteCategory

class WebsiteListView(ListView):
    model = Website
    paginate_by = 25
    template_name = 'websites/index.html'

    def get_queryset(self):
        query_set = super().get_queryset()
        category = self.request.GET.get('categories')
        sort_by_column =  self.request.GET.get('sort')
        if category and category != 'all':
            query_set =  query_set.filter(category__name=category)
        if sort_by_column:
            query_set = query_set.order_by('-' + sort_by_column)
        return query_set

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = WebsiteCategory.objects.all().values_list('name', flat=True)
        return context

class WebsiteDetailView(DetailView):
    model = Website
    template_name = 'websites/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = self.get_object()
        context['category'] = object.category

        context['webpages'] = object.webpage_set.all()
        return context