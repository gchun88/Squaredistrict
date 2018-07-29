from django.db import models

# Create your models here.

class spot_price(models.Model):
    
    bch=models.FloatField()
    bth=models.FloatField()
    eth=models.FloatField()
    ltc=models.FloatField()
    dt=models.DateTimeField(primary_key=True)
    def __float__(self):
        return self.bch
    def __float__(self):
        return self.bth
    def __float__(self):
        return self.eth
    def __float__(self):
        return self.ltc

