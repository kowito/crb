from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from activity.views import calendar_home

admin.autodiscover()
import settings

urlpatterns = patterns('',

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='auth_login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}, name='auth_logout'),
    url(r'^accounts/profile/$', 'crb.views.account_settings', name='account_settings'),


    url(r'^$', login_required(calendar_home), name='home'),

    url(r'^staff/', include('staff.urls')),
    url(r'^room/', include('room.urls')),
    url(r'^academic/', include('academic.urls')),
    url(r'^schedule/', include('activity.urls')),
    url(r'^holiday/', include('holiday.urls')),
    url(r'^report/', include('report.urls')),
    url(r'^transaction/', include('transaction_log.urls')),

    #TODO : Remove when finished design
    url(r'^settings$', 'crb.views.setting', name='system_settings'),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^manage/', include(admin.site.urls)),

)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_URL,
        }),
   )
