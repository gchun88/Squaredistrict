from django.contrib.auth import logout
from django.shortcuts import render
from django.conf import settings

# Create your views here.
from django.http import HttpResponse
from .models import Question
import requests

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
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



def home(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    return render(request, 'polls/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })


from django.shortcuts import redirect












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

