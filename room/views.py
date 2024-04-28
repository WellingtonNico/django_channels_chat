from .models import Room
from django.urls import reverse_lazy
from room.forms import RoomModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView


class RoomCreateView(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('room_list')
    model = Room
    form_class = RoomModelForm


class RoomListView(LoginRequiredMixin, ListView):
    model = Room

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RoomModelForm()
        return context


class RoomDetailView(LoginRequiredMixin, DetailView):
    model = Room
