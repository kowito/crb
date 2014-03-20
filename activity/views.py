from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
from django.template import RequestContext
from django.views.generic.edit import FormView,CreateView,UpdateView
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


from activity.kowito_calandar import HTMLCalendar, SUNDAY
from datetime import date,timedelta,datetime
from itertools import groupby
from crb.utils import add_minute

from models import Activity,ActivityGroup
from forms import ActivityGroupForm
from academic.models import AcademicYear
from transaction_log.models import Transaction
from staff.models import Student
from report.models import ActivityReport,TRANSACTION_STATUS_CHOICES, ActivitySummaryReport
from report.utils import gen_activity_report

class ActivityCalendar(HTMLCalendar):
    def __init__(self, activities):
        super(ActivityCalendar, self).__init__(SUNDAY)
        self.activities = self.group_by_day(activities)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' selected'
            if day in self.activities:
                cssclass += ' filled'
                body = ['<ul class="cal-events">']
                for activity in self.activities[day]:
                    body.append('<li class="important"><img src="/static/admin/img/icon-yes.gif" alt = "%s"></img>/li>' \
                                % (activity.name))
                body.append('</ul>')
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)),self.year, self.month,day)
            return self.day_cell(cssclass, day, self.year, self.month,day)
        return self.day_cell('noday', '&nbsp;', self.year, self.month,day)

    def formatmonth(self, year, month, withyear=True):
        self.year, self.month = year, month
        return super(ActivityCalendar, self).formatmonth(year, month)


    def group_by_day(self, activities):
        field = lambda activity: activity.date.day
        return dict(
            [(day, list(items)) for day, items in groupby(activities, field)]
        )

    def day_cell(self, cssclass, body, syear,smonth,sday):
        return '<td><a href="%s"><span class="cal-day">%s</span></a></td>' % (reverse('calendar_day_url',args=[syear,smonth,sday]),body)


class ActivityAgenda(object):
    def event_cell(start_time,end_time,):
        return ''


class ActivityGroupCreate(CreateView):
    model = ActivityGroup


class ActivityGroupUpdate(UpdateView):
    model = ActivityGroup


@login_required
def create_activity_group(request):
    if request.method == 'POST':
        form = ActivityGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('calendar_home'))
    else:
        form = ActivityGroupForm()

    return render_to_response('activity_group_create_form.html',
                              {'form': form},
                              context_instance=RequestContext(request))


@login_required
def calendar_home(request):
    year,month,day  = date.today().year,date.today().month,date.today().day

    today_activities = Activity.objects.order_by('date').filter(date__year=year, date__month=month, date__day=day)
    activity_list = Activity.objects.order_by('date').filter(date__year=year, date__month=month)
    calendar = ActivityCalendar(activity_list).formatmonth(year, month)

    return render_to_response(
        'calendar_index.html',
        {'calendar': mark_safe(calendar),
         'activity_list': activity_list,
         'today_activities' : today_activities,
         'date': date(year,month,day),
         },
        context_instance=RequestContext(request))


@login_required
def calendar_month(request,year,month):
    year,month = (int(year),int(month))
    today_activities = Activity.objects.order_by('date').filter(date__year=year, date__month=month, date__day=1)
    activity_list = Activity.objects.order_by('date').filter(date__year=year, date__month=month)
    calendar = ActivityCalendar(activity_list).formatmonth(year, month)
    return render_to_response(
        'calendar_index.html',
        {'calendar': mark_safe(calendar),
         'activity_list': activity_list,
         'today_activities' : today_activities,
         'date': date(year,month,1),
         },
        context_instance=RequestContext(request))


@login_required
def calendar_day(request,year,month,day):
    year,month,day = (int(year),int(month),int(day))
    today_activities = Activity.objects.order_by('date').filter(date__year=year, date__month=month, date__day=day)
    activity_list = Activity.objects.order_by('date').filter(date__year=year, date__month=month)
    calendar = ActivityCalendar(activity_list).formatmonth(year, month)
    print day
    return render_to_response(
        'calendar_index.html',
        {'calendar': mark_safe(calendar),
         'activity_list': activity_list,
         'today_activities' : today_activities,
         'date': date(year,month,day),
         },
        context_instance=RequestContext(request))


@login_required
def activity_detail(request,year,month,day,activity_id):
    activity = Activity.objects.get(id=activity_id)
    activity_detail_report, created = ActivitySummaryReport.objects.get_or_create(
        activity=activity,
        year = year,
        month = month,
        )
    activity_report = ActivityReport.objects.filter(activity=activity)
    print activity_detail_report.data

    return render_to_response(
        'activity_detail.html',
        {
        'activity_detail_report' : activity_detail_report,
        'activity_report' : activity_report,
        },
        context_instance=RequestContext(request))