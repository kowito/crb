from django.conf.urls.defaults import url,patterns
from room.views import home, list_model, add_model, modify_model,list_room,ajax_modify_model

urlpatterns = patterns('',
                       url(r'^$', home),
                       url('^room/$', list_room),
                       url('^(?P<model_type>\w+)/$', list_model),
                       url('^(?P<model_type>\w+)/(?P<model_id>\w+)/modify/$', modify_model),
                       url('^(?P<model_type>\w+)/add/$', add_model),
                       url('^(?P<model_type>\w+)/ajax/(?P<model_id>\w+)/modify/$', ajax_modify_model),
                       )
