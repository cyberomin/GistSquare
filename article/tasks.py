import feedparser
import re
import time
import random

from article.models import Article
from article.models import Subscription
from datetime import date, timedelta
from django.core.exceptions import ObjectDoesNotExist
from celery.task import PeriodicTask
from django.utils.timezone import now

from django.template.defaultfilters import slugify
import sendgrid


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

class GetNews(PeriodicTask):
    run_every = timedelta(seconds=7200)

    def run(self,**kwargs):

        URLS = [
                    "http://www.goal.com/en-ng/feeds/news?fmt=rss&ICID=HP",
                    "http://www.theguardian.com/uk/sport/rss",
                    "https://news.google.com/news/feeds?pz=1&cf=all&ned=en_ng&hl=en&topic=s&output=rss",
                    "http://www.uefa.com/rssfeed/uefachampionsleague/rss.xml",
                    "http://www.skysports.com/rss/0,20514,11945,00.xml",
                    "http://allafrica.com/tools/headlines/rdf/sport/headlines.rdf",
                    "http://rss.cnn.com/rss/si_soccer.rss",
                    "http://sports.yahoo.com/soccer/rss.xml",
                    "http://feeds.bbci.co.uk/sport/0/football/rss.xml?edition=uk"
               ]

        d = feedparser.parse(random.choice(URLS))

        for i in range(5):
            title = d.entries[i].title
            body = strip_tags(d.entries[i].summary)

            #Grab any image in the news
            try:
                image = re.search('src="([^"]+)"',d.entries[i].summary)
                img = image.group(1)
            except Exception:
                img = 'null'

            logo = d.feed.image.href
            source = d.feed.title
            slug = slugify(title)

            try:
                article = Article.objects.get(title=title)
            except ObjectDoesNotExist:
                article = Article(title=title,body=body,source=source,logo=logo,image=img,slug=slug)
                #time.sleep(60)
                article.save()
        return True


class RankNews(PeriodicTask):

    run_every = timedelta(seconds=3600)

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
        return True

"""
class SendDailyLetter(PeriodicTask):
    run_every = timedelta(seconds=6000)

    def run(self, **kwargs):

        s = sendgrid.Sendgrid('cyberomin', 'Ropacel1234!', secure=True)

        users = Subscription.objects.all()
        articles = Article.objects.all().order_by("-created_at")[:5]



        sender = ("no-reply@gistsquare.com","Gistsquare")
        message = sendgrid.Message(sender, "Daily Digest", "",body)

        message.add_to("celestineomin@gmail.com", "Celestine Omin")
        message.add_bcc(users)

        s.web.send(message)
"""