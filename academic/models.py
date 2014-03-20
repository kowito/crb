from datetime import datetime

from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.sites.managers import CurrentSiteManager

from academic.extra.fields import DayOfTheWeekField

from room.models import Room
from staff.models import Instructor, Student

class AcademicYear(models.Model):
    year = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __unicode__(self):
        return self.year.__str__()

    class Meta:
        verbose_name = _('academic year')


class Semester(models.Model):
    name = models.CharField(max_length=20)
    academic_year = models.ForeignKey('AcademicYear', related_name ='semester_academic_year')

    def __unicode__(self):
        return '%s, %s' % (self.name,self.academic_year)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _('semester')


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __unicode__(self):
        return '%s : %s' % (self.code,self.name)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _('Course')


class SchoolRoom(models.Model):
    semester= models.ForeignKey('Semester', related_name ='schoolroom_semester')
    course = models.ForeignKey('Course', related_name ='schoolroom_course')
    section_round = models.IntegerField()
    start_date = models.DateField(_('start date'))
    end_date = models.DateField(_('end date'))

    def __unicode__(self):
        return '%s : %s Round' % (self.course,self.section_round)


    class Meta:
        verbose_name = _('Schoolroom')


class PublicationManager(CurrentSiteManager):
    def get_query_set(self):
        return super(CurrentSiteManager, self).get_query_set().filter(publish=True, publish_date__lte=datetime.now())


class Section(models.Model):
    objects = models.Manager()

    # Core fields
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), db_index=True, unique=True)
    description = models.TextField(_('description'))
    schoolroom = models.ForeignKey(SchoolRoom, related_name ='event_schoolroom')

    student = models.ManyToManyField(Student, related_name ='event_student')
    instructor = models.ManyToManyField(Instructor, verbose_name=_('instructor'), blank=True, null=True)

    # Extra fields
    add_date = models.DateTimeField(_('add date'),auto_now_add=True)
    mod_date = models.DateTimeField(_('modification date'), auto_now=True)

    publish_date = models.DateTimeField(_('publication date'), default=datetime.now())
    publish = models.BooleanField(_('publish'), default=True)

    class Meta:
        verbose_name = _('section')
        verbose_name_plural = _('sections')
        get_latest_by = 'id'
        permissions = (("change_instructor", ugettext("Change instructor")),)

    def __unicode__(self):
        return _("%(title)s on %(instructor)s") % { 'title'      : self.title,
                                                    'instructor' : self.instructor }

    def __str__(self):
        return self.__unicode__()

    @models.permalink
    def get_absolute_url(self):
        return ('agenda-detail', (), {
                  'year'  : self.section_date.year,
                  'month' : self.section_date.month,
                  'day'   : self.section_date.day,
                  'slug'  : self.slug })


class SessionPeriod( models.Model):
    section = models.ForeignKey(Section)
    room = models.ForeignKey(Room)
    session_day = DayOfTheWeekField(_('day'))
    start_time = models.TimeField(_('start time'))
    end_time = models.TimeField(_('end time'))

    def __unicode__(self):
        return '%s,%s' % (self.section, self.room)

class Event(models.Model):
    session_period = models.ForeignKey(SessionPeriod, blank=True, null=True)
