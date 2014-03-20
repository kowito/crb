from django.db import models

class HolidayType(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Holiday(models.Model):
    name = models.CharField(max_length=100)
    holiday_type = models.ForeignKey('HolidayType')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.BooleanField()

    def __unicode__(self):
        return self.name
