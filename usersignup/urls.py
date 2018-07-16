from django.urls import path
from usersignup import views

app_name='usersignup'
urlpatterns = [
    path('usersignup/', views.usersignup, name='usersignup'),
]
