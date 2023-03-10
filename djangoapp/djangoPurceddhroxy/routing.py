from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from djangoapp.api.consumers import PacketConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/packets/", PacketConsumer.as_asgi()),
    ])
})