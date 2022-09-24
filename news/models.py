from django.utils import timezone
from django.db import models

class News(models.Model):
    url = models.URLField()
    author = models.CharField(max_length=200, default="mainuser")
    title = models.CharField(max_length=200, default="none")
    body = models.TextField(default="none")
    type = models.CharField(max_length=200, default="none")
    hacker_news_id = models.BigIntegerField(unique=True, default=000)
    origin = models.CharField(max_length=10, default="hackernews")
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)

    def get_comments(self):
        return list(self.comment_set.all())


class Comment(models.Model):
    author = models.CharField(max_length=200, default="mainuser")
    news = models.ForeignKey(News, on_delete=models.CASCADE, null=True)
    text = models.TextField(default="Text")
    type = models.CharField(max_length=200, default="none")
    hacker_comment_id = models.BigIntegerField(unique=True, default=000)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.text)