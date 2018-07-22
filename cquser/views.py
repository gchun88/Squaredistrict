from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, HttpResponse



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
    return render(request, 'polls/main.html', {})

def try1(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,
                                password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'cquser/try.html', {'form': form})
            else:
                return HttpResponse('Disabled account')

        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return redirect('/login/')







from cquser.forms import LoginForm
def user_login(request):
    return render(request, 'cquser/login.html')





