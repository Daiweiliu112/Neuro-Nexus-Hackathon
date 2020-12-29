from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.index, name='index'),
    # path('sign_in/',views.signin,name='sign_in'),
    # path('sign_in_test/',views.signin_test,name='sign_in_test'),
    path('dashboard_uploaded/', views.dashboard, name='dashboard_test'),
    path('dashboard/', views.dashboard_test, name='dashboard'),
    path('child_test/', views.child_image_test, name='child_test'),
    # path('signup/',views.signup,name='signup'),
    path('csv/', views.download_csv, name='download'),
    path('upload/', views.upload_file, name='upload'),
    path(r'ajax/create_meeting/', views.make_meeting, name='create_meeting'),
    # path('clinician/',views.clinician_game,name='clinician'),
    # path('cli/<str:room_name>/',views.clinician_test,name='clinician_test'),
    # path('client/<str:room_name>/',views.client_test,name='client_test'),
    path('cli/<str:room_name>/<int:pk>/<int:client_id>/',
         views.clinician_test, name='clinician_test'),
    path('client/<str:room_name>/<int:pk>/',
         views.client_test, name='client_test'),
    path(r'editview/(?P<pk>\d+)/$', views.edit_view, name='editview'),
    # path('editview/<int:pk>/',views.edit_view,name='editview'),
    path('save_image/', views.save_image_edit, name="save_image_edit"),
    path('create_collection/', views.create_collection_view,
         name="create_collection"),
    path('ajax/create_collection/', views.create_collection,
         name="ajax_create_collection"),
    path(r'edit_collection/(?P<pk>\d+)/$',
         views.edit_collection_view, name='edit_collection'),
    path('client_num/', views.get_client_data, name='client_num'),
    path('check_cli_num/', views.check_cli_num, name='check_cli_num'),
    path('save_cli_data/', views.save_cli_data, name='save_cli_data'),
    path('get_csv/', views.get_csv, name='get_csv'),

    path('spinner/', views.spinner, name='spinner'),
    path('spinner_update', views.spinner_update, name='spinner_update'),

    path('main/', views.main, name='main'),
    path('main2/', views.main2, name='main2'),

    path('pop/', views.pop, name='pop'),
    path('pop_cli/', views.pop_cli, name='pop_cli'),
    path('pop_nvb/', views.pop_nvb, name='pop_nvb'),

    path('light/', views.light, name='light'),
    path('light_cli/', views.light_cli, name='light_cli'),
    path('light_nvb/', views.light_nvb, name='light_nvb'),


    path('pancake/', views.pancake, name='pancake'),
    path('pancake_cli/', views.pancake_cli, name='pancake_cli'),
    path('pancake_nvb/', views.pancake_nvb, name='pancake_nvb'),

    path('cookies/', views.cookies, name='cookies'),

    path('custom_setup/', views.custom_setup, name='custom_setup'),
    path('custom_game', views.custom_game, name='custom_game'),
    path('custom_game_cli', views.custom_game_cli, name='custom_game_cli')

]
