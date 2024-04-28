from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import FormView
from usuarios.forms import CriarContaForm


class CriarContaView(FormView):
    form_class = CriarContaForm
    template_name = "usuarios/criar_conta.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")
