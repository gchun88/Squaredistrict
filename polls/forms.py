from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




from django import forms

class LoginForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


#code below is not working...
class UserForm(forms.ModelForm):
    User = forms.CharField(max_length=20)
    Email = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())





class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
