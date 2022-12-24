import json
from datetime import datetime
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Room,Message
from django.contrib.auth import get_user_model


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)

    async def receive(self,text_data):
        data = json.loads(text_data)
        await self.save_message(data)
        data['type'] = 'chat_message'
        data['date_added'] = datetime.isoformat(datetime.now())
        await self.channel_layer.group_send(self.room_group_name, data)

    async def chat_message(self,event):
        await self.send(text_data=json.dumps(event))

    @sync_to_async
    def save_message(self,data):
        Message.objects.create(
            user=self.scope['user'],
            content=data['message'],
            room=Room.objects.get(slug=data['room'])
        )