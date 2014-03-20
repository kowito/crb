from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.core.urlresolvers import reverse_lazy


from dateutil.parser import parse
from models import Transaction,TransactionUpdateForm
from room.models import Room, Device
from staff.models import Student

class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionUpdateForm
    template_name = "transaction_update_form.html"
    success_url = reverse_lazy('transaction_log_index')

@login_required
def transaction_home(request):

    if request.GET.get('room'):
        transaction_log_list = Transaction.objects.filter(device__room=request.GET['room']).order_by('-timestamp')
    elif request.GET.get('device'):
        transaction_log_list = Transaction.objects.filter(device=request.GET['device']).order_by('-timestamp')
    else:
        transaction_log_list = Transaction.objects.order_by('-timestamp')

    if request.method == 'POST':
        if request.POST.get('search_box'):
            user = Student.objects.filter(
                Q(people__name_th__contains=request.POST.get('search_box')) |\
                Q(people__lastname_th__contains=request.POST.get('search_box'))
                )
            a=[]

            for u in user:
                a.append(u.people.citizen_id)
            transaction_log_list = Transaction.objects.filter(username__in=a).order_by('-timestamp')
        else:
            transaction_log_list = Transaction.objects.order_by('-timestamp')

        if request.POST.get('start_date'):
            transaction_log_list = transaction_log_list.filter(timestamp__range = \
                                                               (parse(request.POST.get('start_date')) \
                                                                ,parse(request.POST.get('end_date')))
                                                               )

    response =  {
        'transaction_log_list' : transaction_log_list,
        'room_list' : Room.objects.filter(),
        'device_list' : Device.objects.filter()
    }
    return render_to_response('transaction_index.html',response, context_instance=RequestContext(request))