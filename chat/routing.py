from django.urls import path, re_path
from chat.consumers import EchoConsumer

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),

    # nginx locate at uri /ws/...
    path('ws/echo/', EchoConsumer.as_asgi()),  # 記得.as_asgi() memo 210816 ISSUE: TypeError: XXX() has no arguments???
    # path('ws/<str:username>/', MessageConsumer.as_asgi())  # self.scope['url_route']['kwargs']['username']
]
