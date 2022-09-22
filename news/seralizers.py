from rest_framework import serializers
from .models import Comment, News

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('title', 'author', 'date_created', 'hacker_news_id')


class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = News
        fields = '__all__'


class CreateNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['title', 'body', 'type', 'hacker_news_id', 'origin']
    
    def save(self, uuid):
        """
            A method overiding DRF serializer's save method
        """
        news = News(
            title = self.validated_data['title'],
            body = self.validated_data['body'],
            type = self.validated_data['type'],
            hacker_news_id = uuid,
            origin = self.validated_data['origin']
        )
        news.save()

        return news


class CreateCommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ['news', 'text', 'type', 'hacker_comment_id']
    
    def save(self, article, uuid):
        """
            A method overiding DRF serializer's save method
        """
        comment = Comment(
            news = article,
            text = self.validated_data['text'],
            type = self.validated_data['type'],
            hacker_comment_id = uuid
        )
        comment.save()

        return comment