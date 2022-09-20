from django.urls import path
from .views import NewsApiListView

urlpatterns = [
    # http://127.0.0.1:8080/api/v0/items/all --> lists all news id from hackernews endpoint
    path('all/', NewsApiListView.as_view(), name='index'),
]