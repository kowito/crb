from django.conf.urls.defaults import url,patterns
from report.views import *

urlpatterns = patterns('',
                       url(r'^$', report_home, name='report_home'),

                       url(r'event/$',
                           report_custom, name='report_custom_url'),
                       
                       url(r'event/custom_group/$',
                           report_custom_activity_group, name='report_custom_activity_group_url'),
                       
                       url(r'event/(?P<year>\d{4})/(?P<month>\w{1,2})/$',
                           report_monthly_activity_group_index, name='report_monthly_activity_group_index_url'),

                       url(r'event/(?P<year>\d{4})/(?P<month>\w{1,2})/(?P<activity_id>\d+)/$',
                           report_monthly_activity_group_detail, name='report_monthly_activity_group_detail_url'),

                       url(r'event/group/(?P<year>\d{4})/(?P<month>\w{1,2})/$',
                           report_group_summary_monthly, name='report_group_summary_monthly_url'),

                       url(r'event/group/(?P<year>\d{4})/(?P<month>\w{1,2})/(?P<pageview>\w+)/$',
                           report_group_summary_monthly, name='report_group_summary_monthly_pageview_url'),

                       url(r'event/group/excel/(?P<year>\d{4})/(?P<month>\w{1,2})/$',
                           report_group_summary_monthly_excel, name='report_group_summary_monthly_excel_url'),

                       url(r'student/(?P<year>\d{4})/(?P<month>\w{1,2})/$',
                           report_monthly_student_index, name='report_monthly_student_index_url'),

                       url(r'student/(?P<year>\d{4})/(?P<month>\w{1,2})/(?P<student_id>\d+)/$',
                           report_monthly_student_detail, name='report_monthly_student_detail_url'),

                       url(r'student/(?P<year>\d{4})/(?P<month>\w{1,2})/(?P<student_id>\d+)/(?P<pageview>\w+)/$',
                           report_monthly_student_detail, name='report_monthly_student_detail_pageview_url'),
                       )
