from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('',views.index,name='index'),
    path('client',views.client_game,name='client'),
    path('clinician',views.clinician_game,name='clinician'),
    path('cli/<str:room_name>/',views.clinician_test,name='clinician_test')
]