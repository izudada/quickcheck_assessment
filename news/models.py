from django.db import models
from datetime import datetime

class News(models.Model):
    url = models.URLField()
    author = models.CharField(max_length=200)
    hacker_news_id = models.BigIntegerField(unique=True, primary_key=True)
    date_created = models.DateTimeField()

    # def save(self, *args, **kwargs):
    #     self.id = self.hackernews # replacing the id(primary key) as the hackernews id
    #     super(News, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.hacker_news_id)