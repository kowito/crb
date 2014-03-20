from django.test import TestCase
from django.db import models
from staff.models import Student, Teacher


class StaffTest(TestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create(title=1, name='name', lastname ='lastname', employee_code='T0001', fingerprint_code=000000000000000001)
        self.student= Student.objects.create(title=1, name='name', lastname ='lastname', student_code='S0001', fingerprint_code=000000000000000002)
    
    def test_teacher(self):
        self.assertEqual(self.teacher.name, 'name')
        self.assertEqual(self.teacher.lastname, 'lastname')
        self.assertEqual(self.teacher.title, 1)
        self.assertEqual(self.teacher.employee_code, 'T0001')
        self.assertEqual(self.teacher.fingerprint_code, 000000000000000001)
        
        self.assertEqual(type(self.teacher.name), str)
        self.assertEqual(type(self.teacher.lastname), str)
        self.assertEqual(type(self.teacher.title), int)
        self.assertEqual(type(self.teacher.employee_code), str)
        self.assertEqual(type(self.teacher.fingerprint_code), int)
        
