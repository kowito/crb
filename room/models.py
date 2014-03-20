from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=100,unique=True)
    status = models.BooleanField()

    def get_absolute_url(self):
        return '/room/building/%s' % self.id

    def __unicode__(self):
        return self.name

    def get_fields(self):
        return [field for field in self._meta.fields]


class Floor(models.Model):
    name = models.CharField(max_length=100)
    building = models.ForeignKey('Building')

    def get_absolute_url(self):
        return '/room/floor/%s' % self.id

    def __unicode__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=100)
    device_code = models.CharField(max_length=100, unique=True)
    fac_id = models.IntegerField(unique=True)
    status = models.BooleanField()
    room = models.ForeignKey('Room',null=True,blank=True)

    def get_absolute_url(self):
        return '/room/device/%s' % self.id

    def __unicode__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=100,unique=True)
    floor = models.ForeignKey('Floor')
    status = models.BooleanField()

    def get_modify_url(self):
        return '/room/room/%s/modify' % self.id

    def __unicode__(self):
        return self.name