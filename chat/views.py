from django.views.generic import TemplateView, FormView
from django.contrib.auth import login
from django.shortcuts import redirect
from chat.forms import CustomUserCreationForm


class SignUp(FormView):
    form_class = CustomUserCreationForm
    template_name = "chat/signup.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("chat")


class Home(TemplateView):
    template_name = "chat/chat.html"
