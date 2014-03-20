from django.contrib import admin
from staff.models import Instructor, Student, People, Title

class TitleAdmin(admin.ModelAdmin):
    list_display = ('title',)


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('title','name_th','lastname_th','email','status')
    list_per_page = 25

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('employee_code','people',)
    list_per_page = 25

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_code','people',)
    list_per_page = 25




admin.site.register(People, PeopleAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Title, TitleAdmin)
