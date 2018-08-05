from django.db import models
from django.utils import timezone
# Create your models here.

class spot_price(models.Model):
    id=models.AutoField(primary_key=True)
    btc=models.FloatField(default=None)
    bch=models.FloatField(default=None)
    eth=models.FloatField(default=None)
    ltc=models.FloatField(default=None)
    dt=models.DateTimeField(default=timezone.now)
    def __float__(self):
        return self.bch
    def __float__(self):
        return self.bth
    def __float__(self):
        return self.eth
    def __float__(self):
        return self.ltc

