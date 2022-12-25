from django.forms import ModelForm
from .models import Room

class RoomModelForm(ModelForm):
    class Meta:
        model = Room
        fields = ('name','slug')
    

    