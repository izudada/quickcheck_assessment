from rest_framework import serializers
from .models import Comment, News

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('title', 'author', 'date_created', 'hacker_news_id')
