from . import views
from django.urls import include, path
from coinqual import views as cViews

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # post views
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('loggedin/', views.loggedin, name="loggedin"),
    path('connection/', views.login, name='loginaf'),
#    path('login/', views.status, name='loggedinaf'),
    path('MyAccount/',cViews.main, name='loggedinaf'),
    path('createaccount/', views.usersignup, name='usersignup'),
]




