from django.urls import path
from .views import SalaListView, SalaMensagensView, SalaCreateView

app_name = "salas"
urlpatterns = [
    path("lista/", SalaListView.as_view(), name="sala_lista"),
    path("criar/", SalaCreateView.as_view(), name="sala_criar"),
    path("<slug:slug>/mensagens/", SalaMensagensView.as_view(), name="sala_mensagens"),
]
