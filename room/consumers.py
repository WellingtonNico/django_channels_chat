from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Room, Message
from django.template.loader import render_to_string


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        if not self.scope["user"].is_authenticated:
            await self.close()
        self.room_slug = self.scope["url_route"]["kwargs"]["room_slug"]
        self.room_group_name = f"chat_{self.room_slug}"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        print(f'Aceitando conexão do usuário {self.scope["user"].username}')
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive_json(self, content, **kwargs):
        """"""
        content["type"] = "chat_message"
        message = await self.save_message(content["message"])
        content["message_html"] = render_to_string(
            "room/partials/message.html", {"message": message, "is_using_socket": True}
        )
        await self.channel_layer.group_send(self.room_group_name, content)

    async def chat_message(self, content):
        await self.send(text_data=content["message_html"])

    @sync_to_async
    def save_message(self, content: str) -> Message:
        """Cria e retorna a mensagem"""

        return Message.objects.create(
            user=self.scope["user"],
            content=content,
            room=Room.objects.get(slug=self.room_slug),
        )
