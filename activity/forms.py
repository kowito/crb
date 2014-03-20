from django import forms
from django.forms import ModelForm, Form
from django.forms.widgets import CheckboxSelectMultiple

from models import ActivityGroup,Activity, REPEAT_DAY_CHOICES, REPEAT_WEEK_CHOICES

from academic.models import AcademicYear


class ActivityGroupForm(ModelForm):

    '''
    repeat_day = forms.ChoiceField(choices=REPEAT_DAY_CHOICES,
                                           help_text='Select repeat Day',
                                           widget=CheckboxSelectMultiple,)
    repeat_week = forms.ChoiceField(choices=REPEAT_WEEK_CHOICES,
                                            help_text='Select repeat Week',
                                            widget=CheckboxSelectMultiple,)
    def clean(self):
        cleaned_data = super(ActivityGroupForm, self).clean()
        repeat_day = cleaned_data.get("repeat_day")
        repeat_week = cleaned_data.get("repeat_week")

        print repeat_day,repeat_week
        return cleaned_data
    '''

    class Meta:
        model = ActivityGroup
        exclude = ('instructor','student','version')

class ActivityForm(ModelForm):
    class Meta:
        model = Activity