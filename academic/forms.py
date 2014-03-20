from django.forms import ModelForm
from academic.models import *

class AcademicYearForm(ModelForm):
    class Meta:
        model = AcademicYear


class SemesterForm(ModelForm):
    class Meta:
        model = Semester


class CourseForm(ModelForm):
    class Meta:
        model = Course


class SchoolRoomForm(ModelForm):
    class Meta:
        model = SchoolRoom


class SectionForm(ModelForm):
    class Meta:
        model = Section