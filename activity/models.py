from django.db import models,transaction
from django.db.models.signals import post_save,pre_save
from django.db.models import Q
from django.dispatch import receiver
from django.utils.translation import ugettext, ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.forms import ModelForm

from dateutil.parser import parse
from dateutil.rrule import rrule, MO, TU, WE, TH, FR, SA, SU, MONTHLY, WEEKLY

from crb.utils import MultiSelectField
from staff.models import Instructor, Student
from academic.models import AcademicYear
from south.modelsinspector import add_introspection_rules


add_introspection_rules(
    [
        (
            (MultiSelectField, ),
            [],
            {
                "verbose_name": ["verbose_name", {"default": None}],
            },
        ),
    ],
    ["^crb.utils.MultiSelectField",])

REPEAT_DAY ={
    1 : SU,
    2 : MO,
    3 : TU,
    4 : WE,
    5 : TH,
    6 : FR,
    7 : SA,
}
REPEAT_DAY_CHOICES =(
    (1 , 'Sunday'),
    (2 , 'Monday'),
    (3 , 'Tuesday'),
    (4 , 'Wednesday'),
    (5 , 'Thursday'),
    (6 , 'Friday'),
    (7 , 'Saturday'),
)
REPEAT_WEEK_CHOICES =(
    (1 , 'Week 1'),
    (2 , 'Week 2'),
    (3 , 'Week 3'),
    (4 , 'Week 4'),
    (5 , 'Week 5'),
)

class ActivityGroup(models.Model):
    name = models.CharField(max_length=120)
    academic_year = models.ForeignKey(AcademicYear)
    start_time = models.TimeField()
    end_time = models.TimeField()
    repeat_day = MultiSelectField(choices=REPEAT_DAY_CHOICES,max_length=100,help_text=_('Select repeat Day'))
    repeat_week = MultiSelectField(choices=REPEAT_WEEK_CHOICES,max_length=100,help_text=_('Select repeat Week'))

    student    = models.ManyToManyField(Student, related_name ='activity_group_student', verbose_name=_('student'),blank=True, null=True)
    instructor = models.ManyToManyField(Instructor, related_name ='activity_group_instructor', verbose_name=_('instructor'), blank=True, null=True)

    late_time = models.TimeField(blank=True, null=True)
    miss_time = models.TimeField(blank=True, null=True)

    version = models.IntegerField(default=1)

    def save(self):
        activity = []
        for repeat_day in self.repeat_day:
            for repeat_week in self.repeat_week:
                activity = activity+list(rrule(MONTHLY,
                                     byweekday=REPEAT_DAY[int(repeat_day)](int(repeat_week)),
                                     dtstart=self.academic_year.start_date,
                                     until=self.academic_year.end_date)
                               )
        activity.sort(key = lambda d: (d.year ,d.month, d.day))

        self.version  = self.version+1
        super(ActivityGroup, self).save()


        Activity.objects.filter(group=self).delete()
        i=1
        for activity_date in activity:

            ac = Activity.objects.create(
                name = "%s : %s" % (self.name,i),
                group = self,
                date = activity_date,
                start_time = self.start_time,
                end_time = self.end_time,
                late_time = self.late_time,
                miss_time = self.miss_time,
                version=self.version
            )
            ac.student = self.student.all()
            ac.instructor = self.instructor.all()
            ac.save()
            i = i+1

        self.version  = self.version+1

    def __unicode__(self):
        return u'%s : %s ' % (self.name,self.academic_year)


class Activity(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=120,blank=True, null=True)
    group = models.ForeignKey(ActivityGroup)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    late_time = models.TimeField(blank=True, null=True)
    actually_start_time = models.TimeField(blank=True, null=True)
    miss_time = models.TimeField(blank=True, null=True)

    student = models.ManyToManyField(Student, related_name ='activity_student',verbose_name=_('student'),blank=True, null=True)
    instructor = models.ManyToManyField(Instructor, related_name ='activity_student', verbose_name=_('instructor'), blank=True, null=True)

    calcled = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    is_report_generated = models.BooleanField(default=False)
    stat_ok = models.IntegerField(blank=True, null=True)
    stat_late = models.IntegerField(blank=True, null=True)
    stat_miss = models.IntegerField(blank=True, null=True)

    version = models.IntegerField(default=1)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('activity_detail_url', args=(self.date.year,self.date.month,self.date.day,self.id))

    def get_overlap_css(self):
        c = Activity.objects.filter(Q(date=self.date),
                                    Q(start_time__range = (self.start_time,self.end_time)) |
                                    Q(end_time__range = (self.start_time,self.end_time))
                                    ).order_by('start_time')
        size = 3 if c.count() > 3 else c.count()
        pos = 1
        for a in c:
            if a.pk == self.pk:
                break
            else :
                pos+=1
        return 'event-%s-on-%s' % (pos,size)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.pk:
            self.version  = self.version+1
        super(Activity, self).save(*args, **kwargs)

    class Meta:
        ordering = ['date']