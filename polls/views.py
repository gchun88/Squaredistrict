from django.contrib.auth import logout
from django.shortcuts import render
from django.conf import settings

# Create your views here.
from django.http import HttpResponse
from .models import Question
import requests

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm

from django.http import HttpResponse
from django.shortcuts import render
from polls.forms import LoginForm


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


from django.http import Http404
from django.shortcuts import render

from .models import Question
# ...
from django.shortcuts import get_object_or_404, render

from .models import Question

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})



from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Choice, Question
# ...
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

def logout_view(request):
    logout(request)
    return render(request,'polls/main.html',{})



def home(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    return render(request, 'polls/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })


from django.shortcuts import redirect





# Create your views here.


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated', 'successfully')
                else:
                    return HttpResponse('Disabled account')

            else:
                return HttpResponse('Invalid login')
        else:
            form = LoginForm()
    return render(request, 'polls/lgin.html', {
        'form': form
    })

def loggedin(request):
    return render(request, 'polls/loggedin.html', {})




from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm


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















def usersignup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main')
    else:
        form = SignUpForm()
    return render(request, 'polls/signup.html', {'form': form})








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

