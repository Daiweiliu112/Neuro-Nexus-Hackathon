from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('',views.index,name='index'),
    path('cli/<str:room_name>/',views.clinician_test,name='clinician_test'),
    path('client/<str:room_name>/',views.client_test,name='client_test')
]