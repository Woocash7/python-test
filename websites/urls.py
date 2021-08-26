from django.urls import path
from websites.views import WebsiteListView, WebsiteDetailView

app_name = 'websites'
urlpatterns = [
    path('', WebsiteListView.as_view(), name='website-list'),
    path('<int:pk>', WebsiteDetailView.as_view(), name='website-detail'),
]