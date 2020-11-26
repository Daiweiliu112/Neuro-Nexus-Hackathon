from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'accounts'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signin2/',views.signin2,name='signin2'),
    path('',views.signin,name="Sign In Main"),
    path('logout/',views.logout_view,name='logout')

]
