from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    source = models.CharField(max_length=200)
    logo = models.TextField(blank=True)
    image = models.TextField(blank=True)
    rank_score = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255, unique=True)

    def __unicode__(self):
        return self.title

class Subscription(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.email

    @classmethod
    def create(cls, email):
        email = cls(email=email)
        return email

class Comments(models.Model):
    article = models.ForeignKey(Article)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    bio = models.TextField(null=True)

    def __unicode__(self):
        return self.user

def create_profile(sender, instance, created, **kwargs):
    if created:
        profile,created = UserProfile.objects.get_or_create(user=instance)

from django.db.models.signals import post_save
post_save.connect(create_profile, sender=User)