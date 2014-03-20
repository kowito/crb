from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from datetime import datetime

from crb.utils import add_minute
from activity.models import Activity, ActivityGroup
from staff.models import Student
from transaction_log.models import Transaction

TRANSACTION_STATUS_CHOICES =(
    ('O','OK'),
    ('L','Late'),
    ('M','Missing'),
    ('I','Invalid'),
)

TRANSACTION_STATUS_BG_COLOR_CHOICES ={
    'O' : 'green-bg',
    'L' : 'orange-bg',
    'M' : 'red-bg',
    'I' : '',
    }


class ActivityReport(models.Model):
    activity = models.ForeignKey(Activity)
    attendance = models.ForeignKey(Student)
    check_in = models.DateTimeField(null=True,blank=True)
    check_out = models.DateTimeField(null=True,blank=True)
    transaction_status = models.CharField(choices=TRANSACTION_STATUS_CHOICES,max_length=1)
    version = models.IntegerField(default=1)

    class Meta:
        get_latest_by = 'version'

    def __unicode__(self):
        return '%s : %s' % (self.activity,self.attendance)

    def tx_bg_color(self):
        return TRANSACTION_STATUS_BG_COLOR_CHOICES[self.transaction_status]

class ActivitySummaryReport(models.Model):
    activity = models.ForeignKey(Activity)
    month = models.IntegerField()
    year = models.IntegerField()
    data = models.TextField()
    generate_date = models.DateTimeField()
    version = models.IntegerField(default=1)
    
    def __unicode__(self):
        try:
            u = '%s : %s' % (self.activity, self.generate_date)
        except :
            u = 'None'
        return u

    def save(self, *args, **kwargs):
        if not self.pk:
            self.generate_date  = datetime.now()
        super(ActivitySummaryReport, self).save(*args, **kwargs)

    class Meta:
        get_latest_by = 'generate_date'