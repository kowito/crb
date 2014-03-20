from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, CreateView
from django.core.urlresolvers import reverse_lazy

from activity.views import calendar_home,activity_detail, calendar_month, calendar_day, create_activity_group
from models import Activity, ActivityGroup
from forms import ActivityForm, ActivityGroupForm

urlpatterns = patterns('',
                       url(r'^$', calendar_home, name='calendar_home'),

                       url(r'(?P<year>\d{4})/(?P<month>\w{1,2})/$',
                           calendar_month, name='calendar_month_url'),

                       url(r'(?P<year>\d{4})/(?P<month>\w{1,2})/(?P<day>\w{1,2})/$',
                           calendar_day, name='calendar_day_url'),

                       url(r'(?P<year>\d{4})/(?P<month>\w{1,2})/(?P<day>\w{1,2})/(?P<activity_id>[0-9]+)/$',
                           activity_detail, name='activity_detail_url'),

                       url(r'^create_activity_group/$', create_activity_group, name='create_activity_group_url'),

                       url(r'^create_activity/$', CreateView.as_view(
                            model=Activity,
                            template_name='activity_create_form.html',
                            ), name='create_activity_url'),
                       )
