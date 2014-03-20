from random import randrange
from datetime import timedelta, datetime

from django.db import models
from django.core.urlresolvers import reverse
from django import forms

from staff.models import People
from room.models import Device

class Transaction(models.Model):
    id = models.AutoField(db_column=u'RN',primary_key=True)
    gid = models.TextField(db_column=u'GID', blank=True)
    fid = models.TextField(db_column=u'FID', blank=True)
    username = models.CharField(max_length=16, db_column=u'UID', blank=True)
    name = models.CharField(max_length=64, db_column=u'Name', blank=True)
    timestamp = models.DateTimeField(null=True, db_column=u'Date', blank=True)
    time = models.CharField(max_length=16, db_column=u'Time', blank=True)
    facid = models.TextField(db_column=u'FacID', blank=True)
    inoutoption = models.TextField(db_column=u'InOutOption', blank=True)
    other = models.IntegerField(null=True, db_column=u'Other', blank=True)

    def get_people(self):
        try :
			people = People.objects.get(citizen_id=self.username)
			return "%s %s" % (people.title,people)
        except:
            #return self.username
            return "Unidentify User : %s" % self.username

    def device(self):
        try:
            fr = Device.objects.get(id=int(self.facid))
        except Exception, e:
            fr = e
        return fr


    def __unicode__(self):
        return '%s %s' % (self.username, self.timestamp)

    def get_absolute_url(self):
        return reverse('transaction_log_detail', kwargs={'pk':self.id})

    class Meta:
        db_table = u'RALog'
        ordering = ['-timestamp']
        get_latest_by = "timestamp"

class TransactionUpdateForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('username', 'timestamp')