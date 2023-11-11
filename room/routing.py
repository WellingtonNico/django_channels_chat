from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path(
        "ws/<slug:room_slug>/", consumers.ChatConsumer.as_asgi(), name="websocket_room"
    )
]
