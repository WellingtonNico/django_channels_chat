from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path(
        "ws/salas/<int:pk>/mensagens/",
        consumers.ChatConsumer.as_asgi(),
        name="sala_mensagens",
    )
]
