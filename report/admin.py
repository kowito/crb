from django.contrib import admin
from report.models import ActivityReport, ActivitySummaryReport

class ActivityReportAdmin(admin.ModelAdmin):
    list_display = ('activity','attendance','check_in','check_out','transaction_status','version')
    list_filter = ('transaction_status','activity')

class ActivitySummaryReportAdmin(admin.ModelAdmin):
    list_display = ('month','year','version')

admin.site.register(ActivityReport,ActivityReportAdmin)
admin.site.register(ActivitySummaryReport,ActivitySummaryReportAdmin)
