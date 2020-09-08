from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'accounts'

urlpatterns = [
    path('home/', views.home, name='Home'),
    path('signup/',views.signup,name='Sign up'),
    path('signin/',views.signin,name='Sign in')

]
