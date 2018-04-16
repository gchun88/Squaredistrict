
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def main(request):
    return render(request, 'polls/main.html')


def login(request):
    return render(request, 'polls/login.html')



LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'main'