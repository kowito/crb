from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib import webdesign
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.template import RequestContext

from staff.models import People, Instructor, Student
from report.models import ActivityReport

STAFF_TYPE = {
              'student' : 1,
              'teacher' : 2,
              }

@login_required
def staff_home(request):
    page_info = {
                 'title' : 'Staff Management',
                 'home_tab' : True
                 }
    student_list = Student.objects.filter(people__status=True)[0:10]
    teacher_list  = Instructor.objects.filter(people__status=True)[0:10]

    response = {
        'student_list': student_list,
        'teacher_list': teacher_list,
        'page_info' : page_info , }

    return render_to_response('staff_index.html',response, context_instance=RequestContext(request))

@login_required
def staff_list(request, staff_type):
    staff = {
        'student': Student.objects.all(),
        'teacher': Instructor.objects.all(),
    }
    page_info = {
                 'title' : staff_type,
                 'teacher_tab' : (True if staff_type=='teacher' else False),
                 'student_tab': (True if staff_type=='student' else False),
                 }
    return render_to_response('staff_list.html',{
        'staff_list' : staff[staff_type],
        'page_info' : page_info ,
        }, context_instance=RequestContext(request))

@login_required
def add_staff(request, staff_type):
    if request.POST :
        form = BuildingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('detail_staff'))
    else:
        form = BuildingForm()
    page_info = {
                 'title' : 'Building',
                 'building_tab' : True,
                 }
    response = {
            'page_info' : page_info ,
            'form' : BuildingForm,
    }
    return render_to_response('modify_template.html',response , context_instance=RequestContext(request))

@login_required
def modify_staff(request, staff_type, building_id):
    if building_id:
        building = Building.objects.get(id=building_id)
    else:
        building = Building()

    if request.POST :
        form = BuildingForm(request.POST, instance=building)
        if form.is_valid():
           form.save()
           return redirect(reverse('detail_staff'))
    else:
        form = BuildingForm(instance=get_object_or_404(Building, id=building_id))

    page_info = {
                 'title' : 'Building',
                 'building_tab' : True
                 }
    response = {'form':form,
        'page_info' : page_info ,
        }
    return render_to_response('modify_template.html',response, context_instance=RequestContext(request))

@login_required
def detail_staff(request, staff_type, staff_id):

    people = get_object_or_404(People,id=staff_id)
    transaction_list = ActivityReport.objects.filter(attendance__people__id=staff_id)
    page_info = {
              'title' : '%s %s' % (people.name_th,people.lastname_th),
              'teacher_tab' : (True if staff_type=='teacher' else False),
              'student_tab': (True if staff_type=='student' else False),
              }
    response = {
              'page_info' : page_info ,
              'people' : people,
              'transaction_list' : transaction_list.order_by("-activity__date"),
              }
    return render_to_response('staff_detail.html',response, context_instance=RequestContext(request))