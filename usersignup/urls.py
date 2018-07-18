from django.urls import path
from usersignup import views

app_name='usersignup'
urlpatterns = [
    path('', views.usersignup, name='usersignup'),
]
