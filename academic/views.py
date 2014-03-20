from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib import webdesign
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.template import RequestContext

from academic.models import *
from academic.forms import *
from crb.utils import make_it_readable

MODEL_TYPE = {
    'academic_year' : AcademicYear,
    'semester' : Semester,
    'course' : Course,
    'schoolroom' : SchoolRoom,
    'section':Section,
}

FORM_TYPE = {
    'academic_year' : AcademicYearForm,
    'semester' : SemesterForm,
    'course' : CourseForm,
    'schoolroom' : SchoolRoomForm,
    'section':SectionForm,
}

@login_required
def schedule(request):
    page_info = {
                 'title' : 'Schedule',
                 'active_tab' : 'home_tab',
                 }
    response = {
        'schedule_list' : None,
    }
    return render_to_response('schedule/schedule_index.html',response, context_instance=RequestContext(request))

@login_required
def course_dashboard(request):
    page_info = {
                 'title' : 'Couese Summary',
                 'home_tab' : True
                 }

    response = {
        'course_list':Course.objects.all(),
        'school_room_list':SchoolRoom.objects.all(),
        'section_list':Section.objects.all(),
        'semester_list':Semester.objects.all(),
        'page_info' : page_info ,
    }
    return render_to_response('academic_index.html',response, context_instance=RequestContext(request))

@login_required
def list_model(request,model_type):
    page_info = {
                 'title' : model_type.replace("_"," "),
                 'active_tab' : model_type
                 }
    model_list = MODEL_TYPE[model_type].objects.all()
    try :
        filed_names = map(make_it_readable, model_list[0]._meta.get_all_field_names())
        filed_names.pop(filed_names.index('id'))
    except IndexError:
        filed_names = None

    return render_to_response('academic_model_lists.html',{
        'filed_names' : filed_names,
        'model_type':model_type,
        'model_list': model_list.values_list(),
        'page_info' : page_info ,
        }, context_instance=RequestContext(request))

@login_required
def add_model(request, model_type):
    success = ''
    if request.POST :
        form = FORM_TYPE[model_type](request.POST)
        if form.is_valid():
            form.save()
            success = "Saved"
    else:
        form = FORM_TYPE[model_type]
    page_info = {
                 'title' : 'Add new %s' % model_type,
                 'active_tab' : model_type,
                 }
    response = {
            'page_info' : page_info ,
            'form' : form,
            'success': success,
            }
    return render_to_response('academic_modify_template.html',response , context_instance=RequestContext(request))

@login_required
def modify_model(request, model_type,model_id):
    if request.POST :
        form = FORM_TYPE[model_type](request.POST,instance=get_object_or_404(MODEL_TYPE[model_type],id=model_id))
        if form.is_valid():
           form.save()
           return redirect('/academic/course/%s/' % (model_type))
    else:
        form = FORM_TYPE[model_type](instance=get_object_or_404(MODEL_TYPE[model_type],id=model_id))
    response = {'form':form,
                'page_info' :{
                    'title' : model_type,
                    'active_tab' : model_type,
                    },
                }
    return render_to_response('academic_modify_template.html',response, context_instance=RequestContext(request))

@login_required
def ajax_modify_model(request, model_type,model_id):
    if request.POST :
        form = FORM_TYPE[model_type](request.POST,instance=get_object_or_404(MODEL_TYPE[model_type],id=model_id))
        if form.is_valid():
            form.save()
    else:
        form = FORM_TYPE[model_type](instance=get_object_or_404(MODEL_TYPE[model_type],id=model_id))
    response = {
        'form':form,
        'available_device':Device.objects.filter(room=None),
        'model_id':model_id,
        'page_info' :{
            'title' : model_type,
            'active_tab' : model_type,
            },
        }
    if(model_type == 'room'):
        return render_to_response('ajax_modify_room_template.html',response, context_instance=RequestContext(request))
    else:
        return render_to_response('ajax_modify_template.html',response, context_instance=RequestContext(request))
