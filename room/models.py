from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse


class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def get_websocket_url(self):
        return f"/ws/rooms/{self.slug}/messages/"

    def get_absolute_url(self):
        return reverse("room_detail", args=(self.slug,))


class Message(models.Model):
    room = models.ForeignKey(Room, related_name="messages", on_delete=models.CASCADE)
    user = models.ForeignKey(
        get_user_model(), related_name="sent_messages", on_delete=models.CASCADE
    )
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("date_added",)
