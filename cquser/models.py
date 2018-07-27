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
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=True)

    
    def __str__(self):
        return self.access_token
    def __str__(self):
        return self.refresh_token
