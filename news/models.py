from django.db import models
from datetime import datetime

class News(models.Model):
    url = models.URLField()
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200, default="none")
    type = models.CharField(max_length=200, default="none")
    hacker_news_id = models.BigIntegerField(unique=True, primary_key=True)
    date_created = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    author = models.CharField(max_length=200)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    text = models.TextField(default="Text")
    type = models.CharField(max_length=200, default="none")
    hacker_news_id = models.BigIntegerField(unique=True, primary_key=True)
    date_created = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.text)