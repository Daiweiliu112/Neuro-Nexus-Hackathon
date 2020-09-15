from django.urls import path
from . import views


app_name = 'main_app'
urlpatterns = [
    path('',views.index,name='index'),
    #path('sign_in/',views.signin,name='sign_in'),
    #path('sign_in_test/',views.signin_test,name='sign_in_test'),
    path('dash_board/',views.dashboard,name='dashboard'),
    path('dashboard/',views.dashboard_test,name='dashboard_test'),
    path('clinician/',views.clinician_image,name='clinician'),
    path('clinician_test/',views.child_image_test,name='clinician_test'),
    path('child/',views.child_image,name='child'),
    path('child_test/',views.child_image_test,name='child_test'),
    #path('signup/',views.signup,name='signup'),
    path('csv/',views.download_csv,name='download')

]