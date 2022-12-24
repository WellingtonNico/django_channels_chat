from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Room
from django.contrib.auth.mixins import LoginRequiredMixin

class RoomListView(LoginRequiredMixin,ListView):
    model = Room

class RoomDetailView(DetailView):
    model = Room
