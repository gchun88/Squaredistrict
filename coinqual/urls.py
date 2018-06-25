"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include, path
from django.contrib import admin
import polls.views as vw


urlpatterns = [
    path('', views.main, name='main'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('', views.logout_view, name='logout'),

    path('coinbase/', views.coinbase, name='coinbase'),
#    path('auth/complete/coinbase/', views.main, name='coinbaselog'),
#    path('auth/complete/coinbase/', views.main, name='getcbcode'),
#    path('auth/', include('social_django.urls', namespace='social')),  # <- Here
    path('home/', vw.home),
    path('auth/complete/coinbase/', views.cb_usr_code)
#    path('auth/complete/coinbase/', views.coinbaselog, name='coinbaselog'),
]

