from django.urls import include, path
from .views import (
                        Index,
                        Article,
                        get_comments
                    )


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<int:pk>/', Article.as_view(), name='article_detail'),
    path('comment/', get_comments, name='comments')
]