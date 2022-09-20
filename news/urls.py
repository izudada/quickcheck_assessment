from django.urls import path
from .views import article_view, NewsApiListView

urlpatterns = [
    # http://127.0.0.1:8080/api/v0/items/all --> lists all news information from hackernews endpoint
    path('all/', NewsApiListView.as_view(), name='index'),

    # http://127.0.0.1:8080/api/v0/items/all --> get an article using its unique hacker news id
    path('item/<int:news_id>', article_view, name='article'),
]