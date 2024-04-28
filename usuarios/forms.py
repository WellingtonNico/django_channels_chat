from django.contrib.auth.forms import UserCreationForm
from usuarios.models import Usuario


class CriarContaForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = (
            "nome",
            "email",
        )
