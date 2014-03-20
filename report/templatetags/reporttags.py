from django import template
from django.utils.safestring import mark_safe

from report.utils import gen_activity_report
from report.models import ActivityReport

register = template.Library()

@register.filter(name="is_user_join_event")
def is_user_join_event(value, arg):

    try:
        ar = ActivityReport.objects.get(attendance=value,activity=arg)
    except:
        gen_activity_report(arg)
        try:
            ar = ActivityReport.objects.get(attendance=value,activity=arg)
        except ActivityReport.DoesNotExist:
            return mark_safe('<small class="tag grey-bg">-</small>')

    return mark_safe('<small class="tag %s">%s</small>' % (ar.tx_bg_color(),ar.get_transaction_status_display()))