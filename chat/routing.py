from django.urls import path
from chat.consumers import EchoConsumer

websocket_urlpatterns = [
<<<<<<< HEAD
=======
    # nginx locate at uri /ws/...
>>>>>>> 5049c4117cdf8d4d170f5425b77076f3ca1f6653
    path('ws/echo/', EchoConsumer.as_asgi()),  # 記得.as_asgi() memo 210816 ISSUE: TypeError: XXX() has no arguments???
    # path('ws/<str:username>/', MessageConsumer.as_asgi())  # self.scope['url_route']['kwargs']['username']
]
