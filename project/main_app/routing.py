from django.urls import re_path
from django.conf.urls import url

from . import consumers , consumers_test

websocket_urlpatters = [
    re_path(r'ws/socket/(?P<room_name>\w+)/$',consumers_test.ChatConsumer),
    #re_path(r'ws/socket/(?P<room_name>\w+)/$',consumers.Consumer)
]