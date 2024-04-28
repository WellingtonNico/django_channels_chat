from django.urls import path
from usuarios.views import CriarContaView

app_name = "usuarios"
urlpatterns = [
    path("criar_conta/", CriarContaView.as_view(), name="criar_conta"),
]
