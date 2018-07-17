from django.urls import path
from django.views.generic import TemplateView
from formsam import views

app_name = 'formsam'
urlpatterns = [
   path('connection/', views.login, name = 'login'),
   path('login/', views.loggedin, name = 'loggedinaf'),
   #path('logout/', views.logout, name = 'logout'),
]

