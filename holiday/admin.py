from django.contrib import admin
from holiday.models import HolidayType,Holiday

class HolidayAdmin(admin.ModelAdmin):
    search_fields = ['name','start_date', 'holiday_type', 'end_date']
    list_display = ('name', 'holiday_type', 'start_date', 'end_date', 'status',)


class HolidayTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)

admin.site.register(Holiday, HolidayAdmin)
admin.site.register(HolidayType, HolidayTypeAdmin)