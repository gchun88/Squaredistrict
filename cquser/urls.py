from django.urls import path
from cquser import views
from django.views.generic import TemplateView
from coinqual import views as vw

app_name='cquser'
urlpatterns = [



    path('signup/', views.signup , name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('try/',views.try1, name='try'),
    path('chain/', views.chain,name='chain'),
]

