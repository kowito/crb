from django.contrib import admin
from django.utils.translation import ugettext as _

from academic.models import AcademicYear, Semester, Course, SchoolRoom, Section, SessionPeriod

class AcademicYearAdmin(admin.ModelAdmin):
    search_fields = ['name']


class SemesterAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'academic_year')


class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name', 'code ']
    list_display = ('name', 'code')


class SchoolRoomAdmin(admin.ModelAdmin):
    search_fields = ['semester', 'course', 'start_date', 'end_date']
    list_display = ('semester', 'course', 'start_date', 'end_date')


class SessionPeriodInline(admin.TabularInline):
    model = SessionPeriod
    extra = 2


class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'schoolroom')
    list_display_links = ('title', )
    list_filter = ('publish', 'instructor', 'schoolroom')
    inlines = [SessionPeriodInline,]
    prepopulated_fields = {"slug": ("title",)}

    search_fields = ('title', 'room__title', 'instructor__people__name', 'instructor__people__lastname', 'schoolroom')

    fieldsets =  ((None, {'fields': ['title', 'slug', 'instructor', 'schoolroom', 'description',]}),
                  (_('Student'), {'classes' : ('collapse',),
                                           'fields'  : ('student',)}),
                  (_('Advanced options'), {'classes' : ('collapse',),
                                           'fields'  : ('publish_date', 'publish')}))


admin.site.register(Section, SectionAdmin)
admin.site.register(AcademicYear, AcademicYearAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(SchoolRoom, SchoolRoomAdmin)
