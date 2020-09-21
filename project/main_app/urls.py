from django.urls import path
from . import views

# app_name = 'main_app'
urlpatterns = [
    path('',views.index,name='index'),
    #path('sign_in/',views.signin,name='sign_in'),
    #path('sign_in_test/',views.signin_test,name='sign_in_test'),
    path('dashboard_uploaded/',views.dashboard,name='dashboard'),
    path('dashboard/',views.dashboard_test,name='dashboard_test'),
    path('clinician/',views.clinician_image,name='clinician'),
    path('clinician_test/',views.clinician_game,name='clinician_test'),
    path('child/',views.child_image,name='child'),
    path('child_test/',views.child_image_test,name='child_test'),
    #path('signup/',views.signup,name='signup'),
    path('csv/',views.download_csv,name='download'),
    path('upload/',views.upload_file,name='upload'),
<<<<<<< HEAD
    path('ajax/create_meeting/',views.make_meeting,name='create_meeting'),

    path('cli/<str:room_name>/',views.clinician_test,name='clinician_test'),
    path('client/<str:room_name>/',views.client_test,name='client_test'),
=======
    path(r'ajax/create_meeting/',views.make_meeting,name='create_meeting'),
    #path('cli/<str:room_name>/',views.clinician_test,name='clinician_test'),
    #path('client/<str:room_name>/',views.client_test,name='client_test')


    path('client/',views.client_game,name='client'),
    #path('clinician/',views.clinician_game,name='clinician'),
    #path('cli/<str:room_name>/',views.clinician_test,name='clinician_test'),
    #path('client/<str:room_name>/',views.client_test,name='client_test'),
    path('cli/<str:room_name>/',views.client_test,name='clinician_test'),
    path('client/<str:room_name>/',views.clinician_test,name='client_test'),
    path('editview/',views.edit_view,name='edit view'),
>>>>>>> master
]