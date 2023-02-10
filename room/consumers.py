from datetime import datetime
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Room,Message


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        print(f'Aceitando conexão do usuário {self.scope["user"].username}')
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)

    async def receive_json(self, content, **kwargs):
        await self.save_message(content)
        content['type'] = 'chat_message'
        content['date_added'] = datetime.isoformat(datetime.now())
        await self.channel_layer.group_send(self.room_group_name, content)

    async def chat_message(self,content):
        await self.send_json(content)

    @sync_to_async
    def save_message(self,data):
        Message.objects.create(
            user=self.scope['user'],
            content=data['message'],
            room=Room.objects.get(slug=data['room'])
        )