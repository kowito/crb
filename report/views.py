from django.template import RequestContext
from django.shortcuts import render_to_response,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db import transaction
from django.db.models import Max
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse 

import datetime
import dateutil

import xlwt

from academic.models import AcademicYear
from transaction_log.models import Transaction
from activity.models import Activity, ActivityGroup
from staff.models import Student
from models import ActivityReport, ActivitySummaryReport
from utils import gen_activity_report, get_percent
from forms import CustomReportForm,CustomSummaryReportForm

@login_required
def report_home(request):
    custom_report_form = CustomReportForm()
    custom_summary_report_form  = CustomSummaryReportForm()
    return render_to_response('report_index.html',
                              {
                                'custom_report_form'  : custom_report_form,
                                'custom_summary_report_form' : custom_summary_report_form,
                               },
                              context_instance=RequestContext(request))
                              
@login_required
def report_custom(request):
    report_redirect ={
        '2':'report_monthly_activity_group_index_url',
        '3':'report_group_summary_monthly_url',
        '4':'report_monthly_student_index_url',
    }
    if request.method == 'POST':
        form = CustomReportForm(request.POST)
        if form.is_valid():
            
            report_date = form.cleaned_data['report_date']
            report_type = form.cleaned_data['report_type']
            return redirect(reverse(report_redirect[report_type],args = [int(report_date.year),int(report_date.month)]))

    else :
        form = CustomReportForm()
    return render_to_response('report_custom.html',
                              {
                                'form' : form,
                                'report_date' : report_date.month,
                                'report_type' : report_type,
                               },
                              context_instance=RequestContext(request))
                              
import dateutil.rrule as dr

@login_required
def report_custom_activity_group(request):
    if request.method == 'POST':
        form = CustomSummaryReportForm(request.POST)
        if form.is_valid():
            report_start_date = form.cleaned_data['report_start_date']
            report_end_date = form.cleaned_data['report_end_date']
            diff = dateutil.relativedelta.relativedelta(report_end_date,report_start_date).months
            if diff > 0 :
                rr = list(dr.rrule(dr.MONTHLY,dtstart=report_start_date, count=diff+1))
                data = []
                for asr in rr:
                    data.append(ActivitySummaryReport.objects.filter(month=asr.month,year=asr.year).order_by('-version')[0])
    return render_to_response('report_custom_activity_group.html',
                              {
                                'report_start_date' : report_start_date,
								'report_end_date' : report_start_date,
                                'diff' : diff,
                                'data':data,
                               },
                              context_instance=RequestContext(request))

@login_required
def report_monthly_activity_group_index(request,year,month):
    activity_group_list = ActivityGroup.objects.all()
    return render_to_response('report_monthly_activity_group_index.html',
                              {
                                'year' : year,
                                'month' : month,
                                'activity_group_list' : activity_group_list,
                               },
                              context_instance=RequestContext(request))

@login_required
def report_group_summary_monthly_excel(request,year,month):
    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet('untitled')

    default_style = xlwt.Style.default_style
    datetime_style = xlwt.easyxf(num_format_str='dd/mm/yyyy hh:mm')
    date_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')
    row = 1

    student_list = Student.objects.all()
    for student in student_list:
        row=row+1
        col=0
        sheet.write(row, col, "%s %s"  % (student.people.name_th,student.people.lastname_th) , style=default_style)
        activity_group_list =  ActivityGroup.objects.filter()
        for activity_group in activity_group_list:
            activity_list = Activity.objects.filter(group=activity_group,date__month=month,date__year=year)
            for activity in activity_list:
                col=col+1
                try :
                    sheet.write(row, col, ("%s" % ActivityReport.objects.get(activity=activity,attendance=student,version=activity.version).transaction_status),style=default_style)

                except ActivityReport.DoesNotExist:
                    sheet.write(row, col, "-",style=default_style)

    response = HttpResponse(mimetype='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=report_group_summary_monthly_excel-%s-%s.xls' % (year,month)
    book.save(response)
    return response

@login_required
def gen_report_group_summary_monthly_version(year,month):
    report_header = ["<thead><tr><th rowspan=2 >Name</th>"]
    activity_group_list =  ActivityGroup.objects.filter()
    activity_header_cell=[]
    summary_report_version=0
    for activity_group in activity_group_list:
        activity_list = Activity.objects.filter(group=activity_group,date__month=month,date__year=year)
        al_count = activity_list.count()
        if al_count:
            report_header.append('<th colspan=%s>%s</th>' % (al_count+1,activity_group.name[0:5]))

        for activity in activity_list:
            gen_activity_report(activity)
            activity_header_cell.append('<th>%s</th>' % activity.date.day)
            summary_report_version += activity.version
        if al_count:
            activity_header_cell.append('<th>sum</th>')

    report_header.append(("<th rowspan=2>Total</th></tr><tr>%s</tr></thead>") % ''.join(activity_header_cell))
    report_table =  ''.join(report_header)
    student_list = Student.objects.filter(status=True)
    student_row = []

    for student in student_list:
        student_row.append("<tr><td>%s %s</td>" % (student.people.name_th,student.people.lastname_th))
        activity_group_list =  ActivityGroup.objects.filter()
        activity_allgroup_status_ok_count = 0
        activity_allgroup_count = 0
        for activity_group in activity_group_list:
            activity_list = Activity.objects.filter(group=activity_group,date__month=month,date__year=year)
            activity_status_ok_count = 0
            for activity in activity_list:
                try :
                    ar = ActivityReport.objects.get(activity=activity,attendance=student,version=activity.version)
                    student_row.append('<td><small class=\"tag %s\">%s</small></td>' % (ar.tx_bg_color(),ar.transaction_status))
                    if ar.transaction_status=='O':
                        activity_status_ok_count +=1
                except ActivityReport.DoesNotExist:
                    student_row.append('<td>-</td>')
            if activity_list.count():
                student_row.append('<td>%s/%s</td>' % (activity_status_ok_count,activity_list.count()))
                activity_allgroup_status_ok_count += activity_status_ok_count
                activity_allgroup_count += activity_list.count()
                activity_status_ok_count=0

        student_row.append('<td>%s/%s : %d&#37;</td>' % (
                                                                activity_allgroup_status_ok_count,
                                                                activity_allgroup_count,
                                                                ((float(activity_allgroup_status_ok_count)/activity_allgroup_count)*100),
                                                                )
                                   )
        student_row.append("</tr>")
    report_table =  report_table+''.join(student_row)
    asr = ActivitySummaryReport.objects.create(
        month = month,
        year = year,
        data = report_table ,
        generate_date = datetime.datetime.now(),
        version = summary_report_version
    )
    return ActivitySummaryReport.objects.get(version = summary_report_version)

@login_required
def report_group_summary_monthly(request,year,month):
    summary_report_version=0
    student_list = Student.objects.filter(status=True)
    activity_group_list =  ActivityGroup.objects.filter()
    for activity_group in activity_group_list:
        activity_list = Activity.objects.filter(group=activity_group,date__month=month,date__year=year)
        for activity in activity_list:
            summary_report_version += activity.version

    if (year == datetime.datetime.now().year) and (month == datetime.datetime.now().month) :
        ar = gen_report_group_summary_monthly_version(year,month)
    else:
        try:
            ar = ActivitySummaryReport.objects.get(month=month,year=year,version=summary_report_version)
        except ActivitySummaryReport.DoesNotExist :
            ar = gen_report_group_summary_monthly_version(year,month)

    return render_to_response('report_monthly_activity_group_summary_detail.html',
                              {
                                'distinct' : "Monthly report group summary",
                                'date' : datetime.datetime(int(year),int(month),1),
                                'year' : year,
                                'month' : month,
                                'report_table' : ar.data,
                                'student_list' : student_list,
                               },
                              context_instance=RequestContext(request))

@login_required
def report_group_summary_monthly(request,year,month,pageview='html'):
    summary_report_version=0
    student_list = Student.objects.filter(status=True)
    activity_group_list =  ActivityGroup.objects.filter()
    for activity_group in activity_group_list:
        activity_list = Activity.objects.filter(group=activity_group,date__month=month,date__year=year)
        for activity in activity_list:
            summary_report_version += activity.version

    if (year == datetime.datetime.now().year) and (month == datetime.datetime.now().month) :
        ar = gen_report_group_summary_monthly_version(year,month)
    else:
        try:
            ar = ActivitySummaryReport.objects.get(month=month,year=year,version=summary_report_version)
        except ActivitySummaryReport.DoesNotExist :
            ar = gen_report_group_summary_monthly_version(year,month)

    if pageview==u'print':
        template = 'report_monthly_activity_group_summary_detail_print.html'
    else:
        template = 'report_monthly_activity_group_summary_detail.html'

    return render_to_response(template,
                              {
                                'distinct' : "Monthly report group summary",
                                'date' : datetime.datetime(int(year),int(month),1),
                                'year' : year,
                                'month' : month,
                                'report_table' : ar.data,
                                'student_list' : student_list,
                               },
                              context_instance=RequestContext(request))

@login_required
def report_monthly_activity_group_detail(request,year,month,activity_id):
    activity_list = (Activity.objects.filter(date__month=month,date__year=year) if activity_id == u'0' else \
                     Activity.objects.filter(group__id=activity_id,date__month=month,date__year=year))
    today = datetime.date.today()
    try:
        caption = ("Event" if activity_id == u'0' else Activity.objects.filter(group__id=activity_id,date__month=month,date__year=year)[0].group)
    except IndexError:
        caption = "Event"
    for activity in activity_list:
        gen_activity_report(activity)

    return render_to_response('report_monthly_activity_group_detail.html',
                              {
                                'caption' : caption,
                                'date' : datetime.datetime(int(year),int(month),1),
                                'year' : year,
                                'month' : month,
                                'activity_list' : activity_list,
                               },
                              context_instance=RequestContext(request))

@login_required
def report_monthly_student_index(request,year,month):
    student_list = Student.objects.filter(people__status=True)
    return render_to_response('report_monthly_student_index.html',
                              {
                                'date' : datetime.datetime(int(year),int(month),1),
                                'year' : int(year),
                                'month' : int(month),
                                'student_list' : student_list,
                               },
                              context_instance=RequestContext(request))

@login_required
def report_monthly_student_detail(request,year,month,student_id,pageview='html'):

    student = get_object_or_404(Student,id=student_id)
    transaction_list = ActivityReport.objects.filter(attendance=student,activity__date__month=month,activity__date__year=year).order_by("-activity__date")
    if pageview==u'print':
        template = 'report_monthly_student_detail_print.html'
    else:
        template = 'report_monthly_student_detail.html'

    return render_to_response(template,
                              {
                                'student' : student,
                                'caption' : "%s%s %s" % (student.people.title,student.people.name_th,student.people.lastname_th),
                                'date' : datetime.datetime(int(year),int(month),1),
                                'year' : year,
                                'month' : month,
                                'transaction_list' : transaction_list,
                               },
                              context_instance=RequestContext(request))
