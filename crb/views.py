from django.shortcuts import render_to_response,redirect
from django.contrib.flatpages.models import FlatPage
from django.contrib.auth import logout
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse 

from staff.models import Student, Instructor

def home(request):
    student_list = Student.objects.filter()
    instructor_list = Instructor.objects.filter()
    return render_to_response('home/index.html',
                              {
                                'student_list': student_list,
                                'instructor_list': instructor_list ,
                                }
                              , context_instance=RequestContext(request))
def account_settings(request):
    return redirect(reverse('calendar_home'))
    #return render_to_response('account_settings.html',
    #                          context_instance=RequestContext(request))

def setting(request):
    return render_to_response('home/setting.html',{
        })

def logout(request):
    logout(request)
    return HttpResponseRedirect("/")
