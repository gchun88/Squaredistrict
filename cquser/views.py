from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, reverse



from .forms import SignUpForm

def signup(request):
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
    return render(request, 'cquser/signup.html', {'form': form})




def logout_view(request):
    logout(request)
    return redirect('main')

def try1(request):
    if request.method == 'POST':
#        form=LoginForm()
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
#            username = request.POST['username']
#            password = request.POST['password']

            user = authenticate(request,username=username,
                                password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request,'polls/main.html', {'form': form})
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('sorry user has no value')
    else:
        return HttpsResponse('sorry No Post')



     #   else:
    #        try:
   #             form = LoginForm(request.POST)
  #          except:
 #               return render(request, 'polls/main.html',{})
#    else:
#        try:
#
#            form = LoginForm()
#        except:
#            return render(request, 'polls/main.html',{})







from cquser.forms import LoginForm
def user_login(request):
    return render(request, 'cquser/login.html')

from cquser.forms import transaction

def chain(request):
    form = transaction()
    return render(request,'cquser/chain.html',{'form2':form})
