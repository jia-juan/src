from django.urls import path
from chat.consumers import EchoConsumer

websocket_urlpatterns = [
    # nginx locate at uri /ws/...
    path('ws/echo/', EchoConsumer.as_asgi()),  # 記得.as_asgi() memo 210816 ISSUE: TypeError: XXX() has no arguments???
    # path('ws/<str:username>/', MessageConsumer.as_asgi())  # self.scope['url_route']['kwargs']['username']
]
