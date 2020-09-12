from django.urls import re_path
from django.conf.urls import url

from . import consumers

websocket_urlpatters = [
    #re_path(r'ws/socket/(?P<room_name>\w+)/$',consumers.Consumer),
    re_path(r'ws/socket/(?P<room_name>\w+)/$',consumers.Consumer)
]