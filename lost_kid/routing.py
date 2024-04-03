from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/lost_kid_messages/$', consumers.LostKidConsumer.as_asgi()),
]
