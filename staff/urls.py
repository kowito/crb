from django.conf.urls.defaults import *
from staff.views import add_staff, staff_list, modify_staff, staff_home, detail_staff
urlpatterns = patterns('',
                       url(r'^$', staff_home, name='staff_home'),
                       url('^(?P<staff_type>\w+)/$', staff_list),
                       url('^(?P<staff_type>\w+)/(?P<staff_id>\d+)/$', detail_staff, name = 'detail_staff'),
                       url('^(?P<staff_type>\w+)/(?P<student_id>\d+)/modify/$', modify_staff),
                       url('^(?P<staff_type>\w+)/add/$', add_staff),
                       )
