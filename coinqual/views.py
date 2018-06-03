from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from django.conf import settings



def main(request):
    return render(request, 'polls/main.html')
def login(request):
    return render(request, 'polls/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'polls/main.html')






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
                            "&redirect_uri=http://127.0.0.1:8000/auth/complete/coinbase/&state=SECURE_RANDOM&scope=wallet:accounts:read")
    return redirect(response.url)





