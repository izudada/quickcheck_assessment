from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Comment, News
from .seralizers import ArticleSerializer, NewsSerializer


class NewsApiListView(ListAPIView):
    """
        Api view that returns a paginated list of all articles
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'type')


@api_view(['GET',])
def article_view(request, news_id):
    """
        Endpoint to get the detail of an article
        and it's corresponding comments
    """
    data = {}
    commment_holder = {}
    comment_array = []
    try:
        article = News.objects.get(hacker_news_id=news_id)
    except News.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    article_serializer = ArticleSerializer(article)
    data['article'] = article_serializer.data

    try:
        comments = Comment.objects.filter(news=article)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    for comment in comments:
        commment_holder['author'] = comment.author
        commment_holder['text'] = comment.text
        commment_holder['type'] = comment.type
        commment_holder['hacker_comment_id'] = comment.hacker_comment_id
        commment_holder['date_created'] = comment.date_created
        comment_array.append(commment_holder)
    data['comment'] = comment_array

    return Response(data)