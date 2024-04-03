# mapapp/routing.py

from django.urls import re_path
from .consumers import LostKidConsumer  # make sure this import statement is correct

websocket_urlpatterns = [
    re_path(r'ws/lost_kid_messages/$', LostKidConsumer.as_asgi()),
]

