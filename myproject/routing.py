# myproject/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from myproject.myproject.routing import websocket_urlpatterns  # <-- Fixed import statement

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
    URLRouter(
      websocket_urlpatterns
    )
  ),
})


def websocket_urlpatterns():
  return None