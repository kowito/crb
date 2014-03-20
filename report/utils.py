from django.db import transaction

from datetime import datetime, date

from crb.utils import add_minute
from staff.models import Student
from transaction_log.models import Transaction
from report.models import ActivityReport, ActivitySummaryReport

from models import TRANSACTION_STATUS_CHOICES

def get_percent(activity_group,student,month,year):
        a = ActivityReport.objects.filter(activity__in=activity_group,
                                          check_in__month = month,
                                          check_in__year = year,
                                          attendance=student)
        b = ActivityReport.objects.filter(activity__in=activity_group,
                                          check_in__month = month,
                                          check_in__year = year,
                                          attendance=student,
                                          transaction_status='O'
                                          )
        return (a.count()/b.count())*100

@transaction.commit_manually
def gen_activity_report(activity):
    start_time = add_minute(activity.start_time,-15)
    start_time = datetime(activity.date.year,activity.date.month,activity.date.day,start_time.hour,start_time.minute)
    end_time = add_minute(activity.end_time ,15)
    end_time = datetime(activity.date.year,activity.date.month,activity.date.day,end_time.hour,end_time.minute)
    if (( not ActivityReport.objects.filter(activity=activity,version=activity.version-1)) \
        and ((activity.date <= date.today()) and (datetime.now() > end_time))):

        late_time = activity.late_time if activity.late_time else add_minute(activity.start_time,15)
        for student in activity.student.all():
            try:
                check_in = Transaction.objects.filter(timestamp__range=(start_time,end_time), \
                                                      username = student.people.citizen_id).order_by('timestamp')[0].timestamp
                check_out= Transaction.objects.filter(timestamp__range=(start_time,end_time), \
                                                      username = student.people.citizen_id).order_by('-timestamp')[0].timestamp
            except:
                check_in,check_out = None,None

            if (check_in == None and check_out == None):
                transaction_status = 'M'
            elif check_in.time() > late_time :
                transaction_status = 'L'
            else :
                transaction_status = 'O'

            ar,created = ActivityReport.objects.get_or_create(activity = activity,
                                                              attendance = student,
                                                              check_in = check_in,
                                                              check_out = check_out,
                                                              transaction_status = transaction_status,
                                                              version = activity.version
                                                              )
            ar.save()
    transaction.commit()
    
    activity.stat_ok = ActivityReport.objects.filter(activity=activity,transaction_status='O').count()
    activity.stat_late = ActivityReport.objects.filter(activity=activity,transaction_status='L').count()
    activity.stat_miss = ActivityReport.objects.filter(activity=activity,transaction_status='M').count()
    
    transaction.commit()

    return ActivityReport.objects.filter(activity=activity)