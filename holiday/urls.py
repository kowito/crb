from django.conf.urls.defaults import url,patterns
from holiday.views import *

urlpatterns = patterns('',
                       )


from holiday.views.holiday_views import *
urlpatterns += patterns('',
    url(
        regex=r'^holiday/archive/$',
        view=HolidayArchiveIndexView.as_view(),
        name='holiday_holiday_archive_index'
    ),
    url(
        regex=r'^holiday/create/$',
        view=HolidayCreateView.as_view(),
        name='holiday_holiday_create'
    ),
    url(
        regex=r'^holiday/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=HolidayDateDetailView.as_view(),
        name='holiday_holiday_date_detail'
    ),
    url(
        regex=r'^holiday/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=HolidayDayArchiveView.as_view(),
        name='holiday_holiday_day_archive'
    ),
    url(
        regex=r'^holiday/(?P<pk>\d+?)/delete/$',
        view=HolidayDeleteView.as_view(),
        name='holiday_holiday_delete'
    ),
    url(
        regex=r'^holiday/(?P<pk>\d+?)/$',
        view=HolidayDetailView.as_view(),
        name='holiday_holiday_detail'
    ),
    url(
        regex=r'^holiday/$',
        view=HolidayListView.as_view(),
        name='holiday_holiday_list'
    ),
    url(
        regex=r'^holiday/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=HolidayMonthArchiveView.as_view(),
        name='holiday_holiday_month_archive'
    ),
    url(
        regex=r'^holiday/today/$',
        view=HolidayTodayArchiveView.as_view(),
        name='holiday_holiday_today_archive'
    ),
    url(
        regex=r'^holiday/(?P<pk>\d+?)/update/$',
        view=HolidayUpdateView.as_view(),
        name='holiday_holiday_update'
    ),
    url(
        regex=r'^holiday/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=HolidayWeekArchiveView.as_view(),
        name='holiday_holiday_week_archive'
    ),
    url(
        regex=r'^holiday/archive/(?P<year>\d{4})/$',
        view=HolidayYearArchiveView.as_view(),
        name='holiday_holiday_year_archive'
    ),
)
