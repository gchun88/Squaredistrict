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
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)






from django.utils import timezone


class transactionM(models.Model):

    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chainid=models.IntegerField(default=1)
    transaction_id=models.AutoField(primary_key=True)
    coin=models.CharField(max_length=10)
    price=models.FloatField(default=None)
    coinamt=models.FloatField(default=None)
    b_s=models.CharField(max_length=10)
    active=models.IntegerField(default=1)
    time=models.DateTimeField(default=timezone.now)















