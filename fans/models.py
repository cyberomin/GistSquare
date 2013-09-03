from django.db import models
from django.contrib.auth.models import User

class Fans(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


