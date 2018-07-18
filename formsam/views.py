from django.http import HttpResponse
from django.shortcuts import render
from formsam.forms import LoginForm


def login(request):
    username = ""

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
    else:
        MyLoginForm = LoginForm()

    return render(request, 'formsam/login.html', {'username': username})


def status(request):
    username = request.POST['username']
    password = request.POST['password']
    return render(request, "formsam/loggedin.html",{'username':username, 'password':password})
