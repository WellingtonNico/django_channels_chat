from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async
from django.shortcuts import get_object_or_404

from .models import Mensagem, Sala
from django.template.loader import render_to_string


class ChatConsumer(AsyncJsonWebsocketConsumer):
    sala_group_name: str
    sala_pk: str

    async def connect(self):
        if not self.scope["user"].is_authenticated:
            await self.close()
        self.sala_pk = self.scope["url_route"]["kwargs"]["pk"]
        self.sala_group_name = f"channel_sala_{self.sala_pk}"
        await self.channel_layer.group_add(
            self.sala_group_name,
            self.channel_name,
        )
        print(f'Aceitando conexão do usuário {self.scope["user"].nome}')
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.sala_group_name, self.channel_name)

    async def receive_json(self, content: dict, **kwargs):
        """
        Recebe o conteúdo da mensagem e cria a mesma,
        retorna a mensagem renderizada para a lista
        """
        content["type"] = "mensagem"
        messagem = await self.salvar_mensagem(content["texto"])
        content["mensagem_html"] = render_to_string(
            "salas/partials/mensagem.html",
            {"messagem": messagem, "is_using_socket": True},
        )
        await self.channel_layer.group_send(self.sala_group_name, content)

    async def mensagem(self, content: dict):
        await self.send(text_data=content["mensagem_html"])

    @sync_to_async
    def salvar_mensagem(self, texto: str) -> Mensagem:
        """Cria e retorna a mensagem"""

        return Mensagem.objects.create(
            usuario_id=self.scope["user"].pk,
            texto=texto,
            sala_id=self.sala_pk,
        )
