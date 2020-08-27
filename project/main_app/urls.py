from django.urls import path
from . import views


app_name = 'main_app'
urlpatterns = [
    path('',views.index,name='index'),
    path('sign_in/',views.signin,name='sign_in'),
    path('dash_board/',views.dashboard,name='dashboard'),
    path('clinician/',views.clinician_image,name='clinician'),
    path('child/',views.child_image,name='child')

]