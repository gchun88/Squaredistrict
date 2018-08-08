from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(label="username",max_length=20,required=True)
    password = forms.CharField(label="password",widget=forms.PasswordInput, required=True)

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


coins=(
    ('btc','Bitcoin'),
    ('bch','Bitcoin Cash'),
    ('eth','Etherium'),
    ('ltc','Litecoin')

)

b_ss=(
    ('b','Buy'),
    ('s','Sell')
)

from cquser.models import transactionM
class transaction(forms.Form):
    b_s=forms.CharField(label='Buy/Sell',widget=forms.Select(choices=b_ss))
    price=forms.FloatField(label='Set your price ')
    coin=forms.CharField(label='Choose your coin ',widget=forms.Select(choices=coins))
    class Meta:
        model=transactionM
        fields=['b_s','price','coin']



