from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from django.conf import settings
from coinbase.wallet.client import OAuthClient
import json
import coinbase
from cquser.forms import LoginForm
from django.contrib.auth import login, authenticate



def main(request):
    return render(request, 'polls/main.html',{})




'''
def login(request):
    return render(request, 'polls/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'polls/main.html')
'''





from django import template
register = template.Library()

@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")



from django.conf import settings #for getting settings vars









from django.conf import settings
import requests





def coinbase(request):
    ClientId = settings.SOCIAL_AUTH_COINBASE_KEY
    clientsecret = settings.SOCIAL_AUTH_COINBASE_SECRET
    response = requests.get("https://www.coinbase.com/oauth/authorize?response_type=code&client_id="+
                            ClientId+
                            "&redirect_uri=http://127.0.0.1:8000/auth/complete/coinbase/&account=all&state=SECURE_RANDOM&scope=wallet:accounts:update wallet:accounts:create wallet:accounts:delete wallet:accounts:read wallet:addresses:create wallet:addresses:read wallet:buys:create wallet:buys:read wallet:checkouts:create wallet:checkouts:read wallet:contacts:read wallet:deposits:create wallet:deposits:read wallet:notifications:read wallet:orders:create wallet:orders:read wallet:orders:refund wallet:payment-methods:delete wallet:payment-methods:limits wallet:payment-methods:read wallet:sells:create wallet:sells:read wallet:transactions:read wallet:transactions:request wallet:transactions:transfer wallet:user:email wallet:user:read wallet:user:update wallet:withdrawals:create wallet:withdrawals:read")
    return redirect(response.url)



from django.template import Context, RequestContext
from django.shortcuts import render_to_response, get_object_or_404


def cb_usr_code(request):
    ClientId = settings.SOCIAL_AUTH_COINBASE_KEY
    clientsecret = settings.SOCIAL_AUTH_COINBASE_SECRET
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    code1=request.GET.get('code')
    context = {
        'code1':code1
    }

    r2=requests.post("https://api.coinbase.com/oauth/token",data={"grant_type":"authorization_code","code":code1,"client_id":ClientId,"client_secret":clientsecret,"redirect_uri":"http://127.0.0.1:8000/auth/complete/coinbase/"})
    cbAFtoken=r2.json()
    client=OAuthClient(cbAFtoken['access_token'],cbAFtoken['refresh_token'])
#    user = client.get_current_user()
#    user_as_json_string = json.dumps(user)
    user=client.get_current_user().name
    price=client.get_spot_price()

    return render_to_response('polls/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'code1':code1,
        'user':user,
        'price':price.amount
    }
        ,
        RequestContext(request))




