from django.forms import ModelForm as mf
from .models import Room

class RoomForm(mf):
    class Meta:
        model =Room
        fields = '__all__'
