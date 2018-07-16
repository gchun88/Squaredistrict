from django import forms

class LoginForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


#code below is not working...
class UserForm(forms.ModelForm):
    User = forms.CharField(max_length=20)
    Email = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())