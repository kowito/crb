from django import forms
from django.utils.translation import ugettext as _

from crb.widget.monthyear import MonthYearWidget

class CustomReportForm(forms.Form):
    REPORT_TYPE = (
       (2, _("Class Report")),
       (3, _("Group Summary Report")),
       (4, _("Student Monthly Report")), 
       )
    report_date = forms.DateField(
        required=False,
        widget=MonthYearWidget(years=xrange(2012,2020))
    )
    report_type = forms.ChoiceField(choices=REPORT_TYPE)
    
class CustomSummaryReportForm(forms.Form):
    report_start_date = forms.DateField(
        required=True,
        widget=MonthYearWidget(years=xrange(2012,2020))
    )
    report_end_date = forms.DateField(
        required=True,
        widget=MonthYearWidget(years=xrange(2012,2020))
    )
