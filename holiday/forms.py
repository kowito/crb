from django.forms import ModelForm
from holiday.models import HolidayType,Holiday

class HolidayTypeForm(ModelForm):
    class Meta:
        model = HolidayType


class HolidayForm(ModelForm):
    class Meta:
        model = Holiday
