from django.urls import path
from django.views.generic import TemplateView
from formsam import views

app_name='formsam'
urlpatterns = [
    path('connection/', views.login, name='loginaf'),
    path('login/', views.status, name='loggedinaf'),
]
