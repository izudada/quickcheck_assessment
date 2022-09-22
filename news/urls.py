from django.urls import path
from .views import (
                        article_view, 
                        comment_create_view,
                        news_create_view, 
                        NewsApiListView
                    )

urlpatterns = [
    # http://127.0.0.1:8080/api/v0/items/all --> lists all news information from hackernews endpoint
    path('all/', NewsApiListView.as_view(), name='index'),

    # http://127.0.0.1:8080/api/v0/items/item/id --> get an article using its unique hacker news id
    path('item/<int:news_id>', article_view, name='article'),

    # http://127.0.0.1:8080/api/v0/items/item --> create an article
    path('item/', news_create_view, name='new_article'),

    path('item/<int:news_id>/comment/', comment_create_view, name='new_comment'),
    
]