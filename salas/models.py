from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django_extensions.db.fields import AutoSlugField


class Sala(models.Model):
    nome = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from="nome")

    def get_websocket_url(self):
        return f"/ws/salas/{self.id}/mensagens/"

    def get_absolute_url(self):
        return reverse("sala_detail", args=(self.slug,))


class Mensagem(models.Model):
    sala = models.ForeignKey(Sala, related_name="mensagens", on_delete=models.CASCADE)
    usuario = models.ForeignKey(
        get_user_model(), related_name="mensagens_enviadas", on_delete=models.CASCADE
    )
    texto = models.TextField()
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("criada_em",)
