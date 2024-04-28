from .models import Sala
from django.urls import reverse_lazy
from salas.forms import SalaModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView


class SalaCreateView(LoginRequiredMixin, CreateView):
    model = Sala
    form_class = SalaModelForm

    def get_success_url(self):
        return reverse_lazy("salas:sala_mensagens", args=(self.object.slug,))


class SalaListView(ListView):
    model = Sala

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SalaModelForm()
        return context


class SalaMensagensView(LoginRequiredMixin, DetailView):
    template_name_suffix = "_mensagens"
    model = Sala
