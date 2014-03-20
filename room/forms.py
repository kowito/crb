from django import forms
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

from room.models import Building, Device,  Floor,  Room

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building


class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor


class RoomForm(forms.ModelForm):
    device = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        queryset =  Device.objects.filter(status=True),

        )

    device.widget.attrs['class'] = 'a-device_checkbox'


    #exclude = ('device',)

    class Meta:
        model = Room



class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
