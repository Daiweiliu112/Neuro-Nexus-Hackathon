from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('',views.index,name='index'),
    #path('sign_in/',views.signin,name='sign_in'),
    #path('sign_in_test/',views.signin_test,name='sign_in_test'),
    path('dashboard_uploaded/',views.dashboard,name='dashboard_test'),
    path('dashboard/',views.dashboard_test,name='dashboard'),
    path('child_test/',views.child_image_test,name='child_test'),
    #path('signup/',views.signup,name='signup'),
    path('csv/',views.download_csv,name='download'),
    path('upload/',views.upload_file,name='upload'),
    path(r'ajax/create_meeting/',views.make_meeting,name='create_meeting'),
    #path('clinician/',views.clinician_game,name='clinician'),
    #path('cli/<str:room_name>/',views.clinician_test,name='clinician_test'),
    #path('client/<str:room_name>/',views.client_test,name='client_test'),
    path('cli/<str:room_name>/',views.clinician_test,name='clinician_test'),
    path('client/<str:room_name>/',views.client_test,name='client_test'),
    path(r'editview/(?P<pk>\d+)/$',views.edit_view,name='editview'),
    #path('editview/<int:pk>/',views.edit_view,name='editview'),
    path('save_image/',views.save_image_edit,name="save_image_edit"),
    path('create_collection/',views.create_collection_view,name="create_collection"),
    path('ajax/create_collection/',views.create_collection,name="ajax_create_collection"),
    path(r'edit_collection/(?P<pk>\d+)/$',views.edit_collection_view,name='edit_collection')
]