from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings



class user_token(models.Model):
    access_token=models.CharField(max_length=80)
    refresh_token=models.CharField(max_length=80)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    req1=models.FloatField(default=None)
    req2=models.FloatField(default=None)
    req3=models.FloatField(default=None)
    req4=models.FloatField(default=None)
    req5=models.FloatField(default=None)
    req6=models.FloatField(default=None)
    req7=models.FloatField(default=None)
    req8=models.FloatField(default=None)
    req9=models.FloatField(default=None)
    req10=models.FloatField(default=None)
    def __str__(self):
        return self.access_token
    def __str__(self):
        return self.refresh_token

from django.utils import timezone


class transactionM(models.Model):

    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chainid=models.CharField(max_length=10)
    transaction_id=models.CharField(max_length=10)
    coin=models.CharField(max_length=10)
    price=models.FloatField(default=None)
    b_s=models.CharField(max_length=10)
    active=models.IntegerField(default=1)
    time=models.DateTimeField(default=timezone.now)






