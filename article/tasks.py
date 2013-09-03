import feedparser
import re
import time
import random

from article.models import Article
from datetime import date, timedelta
from django.core.exceptions import ObjectDoesNotExist
from celery.task import PeriodicTask
from django.utils.timezone import now



from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
"""
class GetNews(PeriodicTask):
    run_every = timedelta(seconds=60)

    def run(self,**kwargs):

        URLS = [
                    "http://www.goal.com/en-ng/feeds/news?fmt=rss&ICID=HP",
                    "http://www.theguardian.com/uk/sport/rss",
                    "https://news.google.com/news/feeds?pz=1&cf=all&ned=en_ng&hl=en&topic=s&output=rss",
                    "http://www.uefa.com/rssfeed/uefachampionsleague/rss.xml"
               ]

        d = feedparser.parse(random.choice(URLS))

        #d = feedparser.parse('http://www.uefa.com/rssfeed/uefachampionsleague/rss.xml')

        for i in range(5):
            title = d.entries[i].title
            body = strip_tags(d.entries[i].summary)

            #Grab any image in the news
            try:
                image = re.search('src="([^"]+)"',d.entries[i].summary)
                img = image.group(1)
            except Exception:
                img = None

            logo = d.feed.image.href
            source = d.feed.title
            try:
                article = Article.objects.get(title=title)
            except ObjectDoesNotExist:
                article = Article(title=title,body=body,source=source,logo=logo,image=img)
                #time.sleep(60)
                article.save()
        return True
"""

class RankNews(PeriodicTask):

    run_every = timedelta(seconds=60)

    def run(self, **kwargs):
        SEC_IN_HOUR = float(60*60)
        GRAVITY = 1.2

        articles = Article.objects.all().order_by("-created_at")
        for article in articles:
            delta = now() - article.created_at
            item_hour_age = delta.total_seconds() // SEC_IN_HOUR
            views = article.views - 1
            article.rank_score = views / pow((item_hour_age + 2),GRAVITY)
            article.save()
        #return True
