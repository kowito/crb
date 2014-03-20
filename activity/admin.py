from django.contrib import admin
from django.utils.translation import ugettext as _

from academic.models import AcademicYear
from models import Activity, ActivityGroup
from forms import ActivityGroupForm

class ActivityGroupAdmin(admin.ModelAdmin):
    list_display = ('name','academic_year','start_time','end_time','version')
    search_fields = ['name']
    #form = ActivityGroupForm


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name','date','start_time','end_time','status', 'stat_ok', 'stat_late', 'stat_miss', 'is_report_generated')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']
    list_per_page = 25


admin.site.register(ActivityGroup, ActivityGroupAdmin)
admin.site.register(Activity, ActivityAdmin)
