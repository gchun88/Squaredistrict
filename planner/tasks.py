from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
from coinbase.wallet.client import OAuthClient
from planner.models import spot_price
from cquser.models import user_token


#@task(name="sum_two_numbers")
#def add(x, y):
#    return x + y
#@task(name="multiply_two_numbers")
##def mul(x, y):
#    total = x * (y * random.randint(3, 100))
#    return total

#@task(name="sum_list_numbers")
#def xsum(numbers):
#    return sum(numbers)



@task(name="priceupdate0")
def priceupdate():
    a=OAuthClient("7676d0b819a701688eef2f52652e8cbcf2107e440c9c11113ae811f38dfac1ed","5d2eec22fd3bc63edd19758a448b14975c0832ab8ca0ac6a1be2c6676c28ec3e")
    spot_price(btc=(float(a.get_buy_price(currency_pair="BTC-USD").amount)),
           eth=(float(a.get_buy_price(currency_pair="ETH-USD").amount)),
           bch=(float(a.get_buy_price(currency_pair="BCH-USD").amount)),
           ltc=(float(a.get_buy_price(currency_pair="LTC-USD").amount)),
           etc=(float(a.get_buy_price(currency_pair="ETC-USD").amount)),
           ).save()

@task(name="token_refresh0")
def get_new_token():
    for i in range(0,len(user_token.objects.all())):
        a=OAuthClient(user_token.objects.values()[i]['access_token'],user_token.objects.values()[i]['refresh_token'])
        a=a.refresh()
        user_token.objects.filter(user_id=user_token.objects.values()[i]['user_id']).update(access_token=a['access_token'],refresh_token=a['refresh_token'])





# buy = spot * 1.0100253114906812
# sell = spot * 0.9900237180312195






