from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib import webdesign
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.template import RequestContext

from room.models import Building, Device,  Floor,  Room
from room.forms import *

MODEL_TYPE = {
    'building' : Building,
    'floor' : Floor,
    'room' : Room,
    'device' : Device
}

FORM_TYPE = {
    'building' : BuildingForm,
    'floor' : FloorForm,
    'room' : RoomForm,
    'device' : DeviceForm
}

@login_required
def home(request):
    page_info = {
                 'title' : 'Conferance Room',
                 'home_tab' : True
                 }
    room_list = Room.objects.all()
    device_list = Device.objects.all();

    return render_to_response('room_index.html',{
        'room_list' : room_list,
        'device_list' : device_list,
        'page_info' : page_info ,
        })

@login_required
def list_room(request):
    page_info = {
                 'title' : 'Conferance Room',
                 'room_tab' : True
                 }
    return render_to_response('room_room_lists.html',{
        'page_info' : page_info ,
        'room_list' : Room.objects.filter(status=True),
        }, context_instance=RequestContext(request))

@login_required
def list_model(request,model_type):
    page_info = {
                 'title' : model_type,
                 'active_tab' : model_type
                 }

    model_list = MODEL_TYPE[model_type].objects.all()

    filed_names = model_list[0]._meta.get_all_field_names()
    filed_names.pop(filed_names.index('id'))
    return render_to_response('room_model_lists.html',{
        'filed_names' : filed_names,
        'model_type':model_type,
        'model_list': model_list.values_list(),
        'page_info' : page_info ,
        }, context_instance=RequestContext(request))

@login_required
def add_model(request, model_type):
    if request.POST :
        form = FORM_TYPE[model_type](request.POST)
        if form.is_valid():
            form.save()
            return redirect('/room/%s/' % model_type)
    else:
        form = FORM_TYPE[model_type]

    page_info = {
                 'title' : 'Add new %s' % model_type,
                 'active_tab' : model_type,
                 }
    response = {
            'page_info' : page_info ,
            'form' : form,
            }
    return render_to_response('modify_template.html',response , context_instance=RequestContext(request))

@login_required
def modify_model(request, model_type,model_id):
    if request.POST :
        form = FORM_TYPE[model_type](request.POST,instance=get_object_or_404(MODEL_TYPE[model_type],id=model_id))
        if form.is_valid():
           form.save()
           return redirect('/room/%s/' % (model_type))
    else:
        form = FORM_TYPE[model_type](instance=get_object_or_404(MODEL_TYPE[model_type],id=model_id))
    response = {'form':form,
                'page_info' :{
                    'title' : model_type,
                    'active_tab' : model_type,
                    },
                'available_device':Device.objects.filter(room=None)
                }
    return render_to_response('modify_template.html',response, context_instance=RequestContext(request))

@login_required
def ajax_modify_model(request, model_type,model_id):
    MODEL_TEMPLATE = {
        'room' : 'ajax_modify_room_template.html',
        'other' : 'ajax_modify_template.html',
    }
    if request.POST :
        form = FORM_TYPE[model_type](request.POST,instance=get_object_or_404(MODEL_TYPE[model_type],id=model_id))
        if form.is_valid():
            form.save()
        else:
            print form.error
    else:
        form = FORM_TYPE[model_type](instance=get_object_or_404(MODEL_TYPE[model_type],id=model_id))

    #Reponse
    response = {
        'form':form,
        'available_device':Device.objects.filter(room=None),
        'model_id':model_id,
        'model_type':model_type,
        }
    return render_to_response(MODEL_TEMPLATE[model_type],response, context_instance=RequestContext(request))
