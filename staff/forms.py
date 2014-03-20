from django.forms import ModelForm
from room.models import Building, Device,  Floor,  Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
