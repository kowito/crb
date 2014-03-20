from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required

from academic.views import schedule, course_dashboard,  list_model, modify_model, add_model, ajax_modify_model
from academic.models import AcademicYear, Semester, Course, SchoolRoom, Section

urlpatterns = patterns('',
                       url(r'courses/$', course_dashboard, name='course_dashboard'),

                       url(r'course/academic_year/$',
                           login_required(ListView.as_view(
                                queryset=AcademicYear.objects.order_by('-year'),
                                context_object_name='academic_year_list',
                                paginate_by = 20,
                                template_name='academic_year_list.html'))
                           , name='academic_yeay_list'),
                       url(r'course/semester/$',
                           login_required(ListView.as_view(
                                queryset=Semester.objects.all(),
                                context_object_name='semester_list',
                                paginate_by = 20,
                                template_name='semester_list.html'))
                           , name='semester_list'),

                       url(r'course/course/$',
                           login_required(ListView.as_view(
                                queryset=Course.objects.all(),
                                context_object_name='course_list',
                                paginate_by = 20,
                                template_name='course_list.html'))
                           , name='course_list'),

                       url(r'course/schoolroom/$',
                           login_required(ListView.as_view(
                                queryset=SchoolRoom.objects.all(),
                                context_object_name='schoolroom_list',
                                paginate_by = 20,
                                template_name='schoolroom_list.html'))
                           , name='schoolroom_list'),
                       url(r'course/section/$',
                           login_required(ListView.as_view(
                                queryset=Section.objects.all(),
                                context_object_name='section_list',
                                paginate_by = 20,
                                template_name='section_list.html'))
                           , name='section_list'),

                       url(r'course/(?P<model_type>\w+)/(?P<model_id>\w+)/modify/$', modify_model, name='academic_modify_model'),
                       url(r'course/(?P<model_type>\w+)/add/$', add_model, name='academic_add_model'),
                       url(r'course/(?P<model_type>\w+)/ajax/(?P<model_id>\w+)/modify/$', ajax_modify_model),
                       )
