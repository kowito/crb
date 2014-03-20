from django.conf.urls.defaults import url,patterns
from django.views.generic import DetailView, CreateView,TemplateView
from django.contrib.auth.decorators import login_required


from transaction_log.models import Transaction
from transaction_log.views import transaction_home,TransactionUpdateView

urlpatterns = patterns('',
                        url(r'^$', transaction_home,name='transaction_log_index'),
                        url(r'^create/$', CreateView.as_view(
                            model=Transaction,
                            template_name='transaction_create_form.html',
                            ), name='transaction_log_create_url'),

                        url(r'^update/(?P<pk>\d+)$', TransactionUpdateView.as_view(), name='transaction_log_update_url'),


                        url(r'^(?P<pk>\d+)/$',
                            login_required(DetailView.as_view(
                                model=Transaction,
                                template_name='transaction_detail.html')),
                            name='transaction_log_detail'),

                        url(r'^/(?P<pk>\d+)/success/$',
                            TemplateView.as_view(
                                template_name='transaction_success.html'),
                            name='transaction_log_success_url'),
                       )
