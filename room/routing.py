from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path(
        "ws/rooms/<slug:room_slug>/messages/",
        consumers.ChatConsumer.as_asgi(),
        name="websocket_room",
    )
]
