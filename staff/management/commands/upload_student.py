# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.db.utils import IntegrityError
from staff.models import Student, People, Title,GENDER_CHOICE
import csv
import re

M = 'นายแพทย์'
F = 'แพทย์หญิง'

class Command(BaseCommand):
    args ='<filename>'
    help = 'Upload student list'

    def clean_gender(self,name):
        return ('M'if name.find(F) else 'F')

    def clean_title(self,name):
        return (Title.objects.get(title=M) if name.find(F) else Title.objects.get(title=F))

    def clean_th_name(self,name):
        name = name.replace(M,'')
        name = name.replace(F,'')
        return name

    def clean_en_name(self,name):
        return name.split()[0].split('.')[1]

    def clean_en_last_name(self, name):
        return name.split()[1]

    def clean_citizen_id(self,citizen_id):
        return re.sub(r"\D", "", citizen_id)

    @transaction.commit_on_success
    def handle(self, *args, **options):
        ifile  = open(args[0], "rb")
        reader = csv.reader(ifile)
        i=0
        for student in reader:
            i=i+1
            try:
                p=People.objects.create(

                    gender = self.clean_gender(student[1]),
                    title = self.clean_title(student[1]),
                    name_th = self.clean_th_name(student[1]),
                    lastname_th = student[2],
                    name_eng = self.clean_en_name(student[4]),
                    lastname_eng = self.clean_en_last_name(student[4]),
                    citizen_id = self.clean_citizen_id(student[6]),
                    fingerprint_code = self.clean_citizen_id(student[6]),
                    email = student[5],
                    status = True
                    )
                #People.Save()
                Student.objects.create(people = p,
                                       student_code = student[0].upper(),
                                       )
                #Student.Save()
                self.stdout.write('%s : Successfully upload Student "%s"\n' % (i,p))
            except Student.DoesNotExist,IntegrityError:
                ifile.close()
                print('Student "%s" failure' % student[0])
                raise CommandError('Student "%s" failure' % args[0])


