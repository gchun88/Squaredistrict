from django.contrib.auth import logout
from django.shortcuts import render, reverse
from django.conf import settings

# Create your views here.
from django.http import HttpResponseRedirect
from .models import Question, Choice
import requests

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})




def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
from django.shortcuts import get_object_or_404, render


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def home(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    return render(request, 'polls/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })






'''
def login(request):
    username = ""

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
    else:
        MyLoginForm = LoginForm()

    return render(request, 'polls/login.html', {'username': username})


def status(request):
    username = request.POST['username']
    password = request.POST['password']
    return render(request, "polls/loggedin.html", {'username':username, 'password':password})
'''





















'''
SOCIAL_AUTH_COINBASE_SCOPE = ['wallet:accounts:read:BTC']
SOCIAL_AUTH_COINBASE_AUTH_EXTRA_ARGUMENTS = {'account': 'BTC'}



from coinbase.wallet.client import Client
import requests





r=requests.get("https://www.coinbase.com/oauth/authorize?response_type=code&client_id="+ClientId+"&redirect_uri=http://www.coinqual.com/buy&state=SECURE_RANDOM&scope=wallet:accounts:read")
code="f4243b8887b87cff93f5185d272d0f5f31e2a5a4df774bed28c0e9953ba17a6c"


r2=requests.post("https://api.coinbase.com/oauth/token",data ={"grant_type":"authorization_code","code":code,"client_id":ClientId,"client_secret":clientsecret,"redirect_uri":"http://www.coinqual.com/buy"})

r=requests.get("https://www.coinbase.com/oauth/authorize?response_type=code&client_id="+ClientId+"&redirect_uri=http://www.coinqual.com/buy&state=SECURE_RANDOM&scope=wallet:accounts:read")
'''

