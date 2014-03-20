from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
	
GENDER_CHOICE= (
    ('M','Male'),
    ('F','Female'),
    ('U','Unspecified'),
)

def get_fingerprint_status(uid):
    return FasUser.objects.get(uid=uid)

class Title(models.Model):
    title = models.CharField(max_length=30)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()


class FasUser(models.Model):
    gid = models.TextField(db_column=u'GID')
    uid = models.CharField(max_length=16, db_column=u'UID')
    name = models.CharField(max_length=64, db_column=u'Name', blank=True)
    utype = models.TextField(db_column=u'UType')
    securitylevel = models.TextField(db_column=u'SecurityLevel')
    finger1 = models.CharField(max_length=3, db_column=u'Finger1', blank=True)
    template1 = models.TextField(db_column=u'Template1', blank=True)
    finger2 = models.CharField(max_length=3, db_column=u'Finger2', blank=True)
    template2 = models.TextField(db_column=u'Template2', blank=True)
    finger3 = models.CharField(max_length=3, db_column=u'Finger3', blank=True)
    template3 = models.TextField(db_column=u'Template3', blank=True)
    admin = models.BooleanField(db_column=u'Admin')
    suspend = models.BooleanField(db_column=u'Suspend')
    password = models.TextField(db_column=u'Password', blank=True)

    class Meta:
        db_table = u'User'


class People(models.Model):
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    title = models.ForeignKey(Title)
    name_th = models.CharField(max_length=125,null=True)
    lastname_th = models.CharField(max_length=125,null=True)
    name_eng = models.CharField(max_length=125,null=True)
    lastname_eng = models.CharField(max_length=125,null=True)
    citizen_id = models.CharField(max_length=13,unique=True,null=True)
    email = models.CharField(max_length=125,null=True)
    status = models.BooleanField()

    def __unicode__(self):
        return '%s %s' % (self.name_th,self.lastname_th)

    def __str__(self):
        return self.__unicode__()

    def is_citizen_id_verify(self):
        import operator
        try :
            p = reduce(operator.add,map(operator.mul,map(int,list(self.citizen_id.__str__()[0:12])),range(13,1,-1)))%11
            parity = 1-p if p<= 1 else 11-p
            verify_code = int(self.citizen_id.__str__()[12])
            return True if verify_code == parity else False
        except :
            return False
			
	def clean(self, *args, **kwargs):
		if not bool(FasUser.objects.filter(uid=self.citizen_id)):
			raise ValidationError('No user citizen id apper in system please try again')
        super(People, self).clean(*args, **kwargs)

    def full_clean(self, *args, **kwargs):
        return self.clean(*args, **kwargs)

	def save(self, *args, **kwargs):
		self.full_clean()
		super(People, self).save(*args, **kwargs)
		
    class Meta:
        verbose_name = _('Staff')



class Student(models.Model):
    people = models.OneToOneField(People)
    student_code = models.CharField(max_length=6)
    status = models.BooleanField()

    def __unicode__(self):
        return '%s:%s %s' % (self.student_code, self.people.name_th,self.people.lastname_th)

    def __str__(self):
        return self.__unicode__()

    def get_absolute_url(self):

        return reverse('detail_staff',args=(2,self.id))

    class Meta:
        verbose_name = _('Student')


class Instructor(models.Model):
    people = models.OneToOneField(People)
    employee_code = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        return '%s %s' % (self.people.name_th,self.people.lastname_th)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _('Instructor')