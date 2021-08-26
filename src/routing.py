# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.security.websocket import AllowedHostsOriginValidator
#
# from chat.routing import websocket_urlpatterns

# application = ProtocolTypeRouter({
#     'websocket': AllowedHostsOriginValidator(  # 繼承settings.ALLOWED_HOSTS
#         AuthMiddlewareStack(
#             URLRouter(
#                 websocket_urlpatterns
#             )
#         ),
#     )
# })