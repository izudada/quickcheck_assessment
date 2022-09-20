from django_cron import CronJobBase, Schedule
import requests
from .models import Comment, News
from datetime import datetime


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 5 # every 5 minutes
    RETRY_AFTER_FAILURE_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'news.my_cron_job'    # a unique code

    def do(self):
        """
            A function to 
        """

        NEWS_URL = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty' # external endpoint that returns list of ids

        headers = {'user-agent': 'quickcheck/0.0.1'}
        response = requests.get(NEWS_URL, headers=headers)

        count = 0
        for i in response.json():
            # lopping the array of article ids to get their needed details
            url = " empty"
            article_url = f"https://hacker-news.firebaseio.com/v0/item/{i}.json?print=pretty"
            response = requests.get(article_url, headers=headers)
            ts = datetime.fromtimestamp(response.json()["time"])

            try:
                url = response.json()["url"]
            except Exception as e:
                print(e)
                url = "Empty"

            news_id = News(
                    url=url,
                    author = response.json()["by"],
                    title = response.json()["title"],
                    type = response.json()["type"],
                    hacker_news_id = i,
                    date_created = ts,
                )
            news_id.save()

            #  If article has kids/comments get the details and save to database
            try:
                kids = response.json()["kids"]
                for kid in kids:
                    comment_url = f"https://hacker-news.firebaseio.com/v0/item/{kid}.json?print=pretty"
                    response = requests.get(comment_url, headers=headers)
                    ts = datetime.fromtimestamp(response.json()["time"])
                    comment = Comment(
                        author = response.json()["by"],
                        news = news_id,
                        text = response.json()["text"],
                        type = response.json()["type"],
                        hacker_news_id = kid,
                        date_created = ts,
                    )
                    comment.save()
            except Exception as e:
                print(e)

            if count >= 100:
                break

            count += 1
