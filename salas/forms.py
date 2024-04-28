from crispy_forms.helper import FormHelper
from django.forms import ModelForm
from .models import Sala


class SalaModelForm(ModelForm):

    class Meta:
        model = Sala
        fields = ("nome",)
