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
from planner.models import spot_price

from cquser.forms import transaction



cities = [1,2,3,4,5,6,7,'wef']
tsdata=['b_s','price','coin','coinamt']

from cquser.models import transactionM
import re
from django.contrib.auth.models import User
from cquser.forms import LoginForm
def main(request):

    
    if request.method == "POST" :
        form=transaction(request.POST)
        if form.is_valid():
            b_s1 = form.cleaned_data.get(tsdata[0])
            price1 = form.cleaned_data.get(tsdata[1])
            coin1 = form.cleaned_data.get(tsdata[2])
            coinamt1 = form.cleaned_data.get(tsdata[3])

            try:
                string=transactionM.objects.order_by('-chainid').values()[0]+1
            except:
                string = 1

            user1=request.user
            if len([price1])>1:
                for i in range(0,len([price1])):
                    transactionM(chainid=string[0], coin=coin1[i], price=float(price1[i]), coinamt=float(coinamt1[i]), b_s=b_s1[i],
                                 user=user1[0]).save()
                return HttpResponseRedirect(revser('main'))
            else:
                transactionM(chainid=string,coin=coin1,price=float(price1),coinamt=float(coinamt1),b_s=b_s1,user=user1).save()
                return HttpResponseRedirect(reverse('main'))

        loginform=LoginForm(request.POST)
        if loginform.is_valid():
            username=loginform.cleaned_data.get('username')
            password=loginform.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                else:
                    return HttpResponse('disabled account')
    if request.user.is_authenticated:
        records = transactionM.objects.filter(active=1,user_id=User.objects.filter(username=request.user)[0]).order_by('time')
    else:
        records=[]
    try:
        trst_id=[re.sub("[a-z]| ","",a) for a in request.POST if "close" in a]
        transactionM.objects.filter(transaction_id=int(trst_id[0])).delete()

    except:
        print("hi")
    Cprice = spot_price.objects.order_by('-id').values_list('btc',flat=True)[0]
    context={'Cpirce':round(Cprice/1.0100253114906812,2),
             'cities':cities,
             'records':records,}

    return render(request, 'polls/main.html',context)




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
                            "&redirect_uri=http://www.coinqual.com/coinbase/&account=all&state=SECURE_RANDOM&scope=wallet:accounts:update wallet:accounts:create wallet:accounts:delete wallet:accounts:read wallet:addresses:create wallet:addresses:read wallet:buys:create wallet:buys:read wallet:checkouts:create wallet:checkouts:read wallet:contacts:read wallet:deposits:create wallet:deposits:read wallet:notifications:read wallet:orders:create wallet:orders:read wallet:orders:refund wallet:payment-methods:delete wallet:payment-methods:limits wallet:payment-methods:read wallet:sells:create wallet:sells:read wallet:transactions:read wallet:transactions:request wallet:transactions:transfer wallet:user:email wallet:user:read wallet:user:update wallet:withdrawals:create wallet:withdrawals:read")
    return redirect(response.url)



from django.template import Context, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from cquser.models import user_token

def cb_usr_code(request):
    ClientId = settings.SOCIAL_AUTH_COINBASE_KEY
    clientsecret = settings.SOCIAL_AUTH_COINBASE_SECRET
    code1=request.GET.get('code')
    r2=requests.post("https://api.coinbase.com/oauth/token",data={"grant_type":"authorization_code","code":code1,"client_id":ClientId,"client_secret":clientsecret,"redirect_uri":"http://www.coinqual.com/coinbase/"})
    cbAFtoken=r2.json()
#        client=OAuthClient(cbAFtoken['access_token'],cbAFtoken['refresh_token'])
    try:
        if len(user_token.objects.filter(user=request.user).values()[0]['access_token'])>1:
            user_token.objects.filter(user=request.user).update(access_token=cbAFtoken['access_token'],refresh_token=cbAFtoken['refresh_token'])
            clito=user_token.objects.filter(user=request.user).values()[0]
            client=OAuthClient(clito['access_token'],clito['refresh_token'])
        else:
            user_token(user=request.user,access_token=cbAFtoken['access_token'],refresh_token=cbAFtoken['refresh_token'])
            clito=user_token.objects.filter(user=request.user).values()[0]
            client=OAuthClient(clito['access_token'],clito['refresh_token'])
        user=client.get_current_user().name
        price=client.get_spot_price().amount
    except:
        client=[]
        user=[]
        price=[]

#    if request.user is not 'ananymous' or request.user is not None:
#        if client is None:
#            user_token(access_token=abAFtoken['access_token'],refresh_token=abAFtoken['refresh_token'],user_id=request.user)

#    user = client.get_current_user()
#    user_as_json_string = json.dumps(user)

#    CBtoken(access_token=cbAFtoken['access_token'],refresh_token=cbAFtoken['refresh_token']).save()
    context={
    'code1':code1,
    'user':user,
    'price':price,}
#    return redirect('main')
    return render(request,'polls/home.html',context)


