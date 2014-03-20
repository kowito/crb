# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Application(models.Model):
    appid = models.TextField(db_column=u'AppID') # Field name made lowercase. This field type is a guess.
    appdescription = models.CharField(max_length=128, db_column=u'AppDescription', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Application'

class Apppwdfiller(models.Model):
    uid = models.CharField(max_length=16, db_column=u'UID') # Field name made lowercase.
    appid = models.TextField(db_column=u'AppID') # Field name made lowercase. This field type is a guess.
    appusername = models.CharField(max_length=64, db_column=u'AppUserName', blank=True) # Field name made lowercase.
    apppassword = models.TextField(db_column=u'AppPassword', blank=True) # Field name made lowercase. This field type is a guess.
    enable = models.BooleanField(db_column=u'Enable') # Field name made lowercase.
    apfid = models.AutoField(db_column=u'ApfID') # Field name made lowercase.
    class Meta:
        db_table = u'AppPwdFiller'

class Facdefinition(models.Model):
    facid = models.TextField(db_column=u'FacID') # Field name made lowercase. This field type is a guess.
    facip = models.CharField(max_length=16, db_column=u'FacIP') # Field name made lowercase.
    description = models.CharField(max_length=64, db_column=u'Description', blank=True) # Field name made lowercase.
    flag = models.TextField(db_column=u'Flag') # Field name made lowercase. This field type is a guess.
    port_c = models.IntegerField(null=True, db_column=u'Port_C', blank=True) # Field name made lowercase.
    port_s = models.IntegerField(null=True, db_column=u'Port_S', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'FacDefinition'

class Group(models.Model):
    gid = models.TextField(db_column=u'GID') # Field name made lowercase. This field type is a guess.
    groupname = models.CharField(max_length=64, db_column=u'GroupName') # Field name made lowercase.
    uid = models.CharField(max_length=16, db_column=u'UID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Group'

class Permission(models.Model):
    pn = models.AutoField(db_column=u'PN') # Field name made lowercase.
    gid = models.TextField(db_column=u'GID', blank=True) # Field name made lowercase. This field type is a guess.
    uid = models.CharField(max_length=16, db_column=u'UID', blank=True) # Field name made lowercase.
    facid = models.TextField(db_column=u'FacID', blank=True) # Field name made lowercase. This field type is a guess.
    day1 = models.TextField(db_column=u'Day1', blank=True) # Field name made lowercase. This field type is a guess.
    month1 = models.TextField(db_column=u'Month1', blank=True) # Field name made lowercase. This field type is a guess.
    weekday1 = models.TextField(db_column=u'WeekDay1', blank=True) # Field name made lowercase. This field type is a guess.
    time1 = models.CharField(max_length=6, db_column=u'Time1', blank=True) # Field name made lowercase.
    day2 = models.TextField(db_column=u'Day2', blank=True) # Field name made lowercase. This field type is a guess.
    month2 = models.TextField(db_column=u'Month2', blank=True) # Field name made lowercase. This field type is a guess.
    weekday2 = models.TextField(db_column=u'WeekDay2', blank=True) # Field name made lowercase. This field type is a guess.
    time2 = models.CharField(max_length=6, db_column=u'Time2', blank=True) # Field name made lowercase.
    enable = models.BooleanField(db_column=u'Enable') # Field name made lowercase.
    option1 = models.IntegerField(null=True, db_column=u'Option1', blank=True) # Field name made lowercase.
    option2 = models.IntegerField(null=True, db_column=u'Option2', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Permission'

class Ralog(models.Model):
    rn = models.AutoField(db_column=u'RN') # Field name made lowercase.
    gid = models.TextField(db_column=u'GID', blank=True) # Field name made lowercase. This field type is a guess.
    fid = models.TextField(db_column=u'FID', blank=True) # Field name made lowercase. This field type is a guess.
    uid = models.CharField(max_length=16, db_column=u'UID', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=64, db_column=u'Name', blank=True) # Field name made lowercase.
    date = models.DateTimeField(null=True, db_column=u'Date', blank=True) # Field name made lowercase.
    time = models.CharField(max_length=16, db_column=u'Time', blank=True) # Field name made lowercase.
    facid = models.TextField(db_column=u'FacID', blank=True) # Field name made lowercase. This field type is a guess.
    inoutoption = models.TextField(db_column=u'InOutOption', blank=True) # Field name made lowercase. This field type is a guess.
    other = models.IntegerField(null=True, db_column=u'Other', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RALog'

class Session(models.Model):
    gid = models.TextField(db_column=u'GID', blank=True) # Field name made lowercase. This field type is a guess.
    instart = models.CharField(max_length=6, db_column=u'InStart', blank=True) # Field name made lowercase.
    instop = models.CharField(max_length=6, db_column=u'InStop', blank=True) # Field name made lowercase.
    outstart = models.CharField(max_length=6, db_column=u'OutStart', blank=True) # Field name made lowercase.
    outstop = models.CharField(max_length=6, db_column=u'OutStop', blank=True) # Field name made lowercase.
    sid = models.AutoField(db_column=u'SID') # Field name made lowercase.
    class Meta:
        db_table = u'Session'

class Talog(models.Model):
    gid = models.TextField(db_column=u'GID', blank=True) # Field name made lowercase. This field type is a guess.
    uid = models.CharField(max_length=16, db_column=u'UID', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=64, db_column=u'Name', blank=True) # Field name made lowercase.
    date = models.DateTimeField(null=True, db_column=u'Date', blank=True) # Field name made lowercase.
    intime = models.CharField(max_length=16, db_column=u'InTime', blank=True) # Field name made lowercase.
    date2 = models.DateTimeField(null=True, db_column=u'Date2', blank=True) # Field name made lowercase.
    outtime = models.CharField(max_length=16, db_column=u'OutTime', blank=True) # Field name made lowercase.
    tn = models.AutoField(db_column=u'TN') # Field name made lowercase.
    class Meta:
        db_table = u'TALog'

class User(models.Model):
    gid = models.TextField(db_column=u'GID') # Field name made lowercase. This field type is a guess.
    uid = models.CharField(max_length=16, db_column=u'UID') # Field name made lowercase.
    name = models.CharField(max_length=64, db_column=u'Name', blank=True) # Field name made lowercase.
    utype = models.TextField(db_column=u'UType') # Field name made lowercase. This field type is a guess.
    securitylevel = models.TextField(db_column=u'SecurityLevel') # Field name made lowercase. This field type is a guess.
    finger1 = models.CharField(max_length=3, db_column=u'Finger1', blank=True) # Field name made lowercase.
    template1 = models.TextField(db_column=u'Template1', blank=True) # Field name made lowercase. This field type is a guess.
    finger2 = models.CharField(max_length=3, db_column=u'Finger2', blank=True) # Field name made lowercase.
    template2 = models.TextField(db_column=u'Template2', blank=True) # Field name made lowercase. This field type is a guess.
    finger3 = models.CharField(max_length=3, db_column=u'Finger3', blank=True) # Field name made lowercase.
    template3 = models.TextField(db_column=u'Template3', blank=True) # Field name made lowercase. This field type is a guess.
    admin = models.BooleanField(db_column=u'Admin') # Field name made lowercase.
    suspend = models.BooleanField(db_column=u'Suspend') # Field name made lowercase.
    password = models.TextField(db_column=u'Password', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'User'

