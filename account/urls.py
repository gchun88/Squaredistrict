from django.conf.urls import url
from . import views
from django.urls import include, path

urlpatterns = [
    # post views
    path('login/', views.user_login, name='login'),
]