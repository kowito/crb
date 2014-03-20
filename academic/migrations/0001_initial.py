# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AcademicYear'
        db.create_table('academic_academicyear', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('academic', ['AcademicYear'])

        # Adding model 'Semester'
        db.create_table('academic_semester', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('academic_year', self.gf('django.db.models.fields.related.ForeignKey')(related_name='semester_academic_year', to=orm['academic.AcademicYear'])),
        ))
        db.send_create_signal('academic', ['Semester'])

        # Adding model 'Course'
        db.create_table('academic_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('academic', ['Course'])

        # Adding model 'SchoolRoom'
        db.create_table('academic_schoolroom', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('semester', self.gf('django.db.models.fields.related.ForeignKey')(related_name='schoolroom_semester', to=orm['academic.Semester'])),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(related_name='schoolroom_course', to=orm['academic.Course'])),
            ('section_round', self.gf('django.db.models.fields.IntegerField')()),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('academic', ['SchoolRoom'])

        # Adding model 'Section'
        db.create_table('academic_section', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('schoolroom', self.gf('django.db.models.fields.related.ForeignKey')(related_name='event_schoolroom', to=orm['academic.SchoolRoom'])),
            ('add_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('mod_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 12, 3, 0, 0))),
            ('publish', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('academic', ['Section'])

        # Adding M2M table for field student on 'Section'
        db.create_table('academic_section_student', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('section', models.ForeignKey(orm['academic.section'], null=False)),
            ('student', models.ForeignKey(orm['staff.student'], null=False))
        ))
        db.create_unique('academic_section_student', ['section_id', 'student_id'])

        # Adding M2M table for field instructor on 'Section'
        db.create_table('academic_section_instructor', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('section', models.ForeignKey(orm['academic.section'], null=False)),
            ('instructor', models.ForeignKey(orm['staff.instructor'], null=False))
        ))
        db.create_unique('academic_section_instructor', ['section_id', 'instructor_id'])

        # Adding model 'SessionPeriod'
        db.create_table('academic_sessionperiod', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['academic.Section'])),
            ('room', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['room.Room'])),
            ('session_day', self.gf('academic.extra.fields.DayOfTheWeekField')(max_length=1)),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('academic', ['SessionPeriod'])

        # Adding model 'Event'
        db.create_table('academic_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('session_period', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['academic.SessionPeriod'], null=True, blank=True)),
        ))
        db.send_create_signal('academic', ['Event'])


    def backwards(self, orm):
        # Deleting model 'AcademicYear'
        db.delete_table('academic_academicyear')

        # Deleting model 'Semester'
        db.delete_table('academic_semester')

        # Deleting model 'Course'
        db.delete_table('academic_course')

        # Deleting model 'SchoolRoom'
        db.delete_table('academic_schoolroom')

        # Deleting model 'Section'
        db.delete_table('academic_section')

        # Removing M2M table for field student on 'Section'
        db.delete_table('academic_section_student')

        # Removing M2M table for field instructor on 'Section'
        db.delete_table('academic_section_instructor')

        # Deleting model 'SessionPeriod'
        db.delete_table('academic_sessionperiod')

        # Deleting model 'Event'
        db.delete_table('academic_event')


    models = {
        'academic.academicyear': {
            'Meta': {'object_name': 'AcademicYear'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'academic.course': {
            'Meta': {'object_name': 'Course'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'academic.event': {
            'Meta': {'object_name': 'Event'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'session_period': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['academic.SessionPeriod']", 'null': 'True', 'blank': 'True'})
        },
        'academic.schoolroom': {
            'Meta': {'object_name': 'SchoolRoom'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'schoolroom_course'", 'to': "orm['academic.Course']"}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section_round': ('django.db.models.fields.IntegerField', [], {}),
            'semester': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'schoolroom_semester'", 'to': "orm['academic.Semester']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'academic.section': {
            'Meta': {'object_name': 'Section'},
            'add_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['staff.Instructor']", 'null': 'True', 'blank': 'True'}),
            'mod_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 12, 3, 0, 0)'}),
            'schoolroom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'event_schoolroom'", 'to': "orm['academic.SchoolRoom']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'student': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'event_student'", 'symmetrical': 'False', 'to': "orm['staff.Student']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'academic.semester': {
            'Meta': {'object_name': 'Semester'},
            'academic_year': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'semester_academic_year'", 'to': "orm['academic.AcademicYear']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'academic.sessionperiod': {
            'Meta': {'object_name': 'SessionPeriod'},
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['room.Room']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['academic.Section']"}),
            'session_day': ('academic.extra.fields.DayOfTheWeekField', [], {'max_length': '1'}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        'room.building': {
            'Meta': {'object_name': 'Building'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'room.floor': {
            'Meta': {'object_name': 'Floor'},
            'building': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['room.Building']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'room.room': {
            'Meta': {'object_name': 'Room'},
            'floor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['room.Floor']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'staff.instructor': {
            'Meta': {'object_name': 'Instructor'},
            'employee_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'people': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['staff.People']", 'unique': 'True'})
        },
        'staff.people': {
            'Meta': {'object_name': 'People'},
            'citizen_id': ('django.db.models.fields.CharField', [], {'max_length': '13', 'unique': 'True', 'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True'}),
            'fingerprint_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True', 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname_eng': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True'}),
            'lastname_th': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True'}),
            'name_th': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['staff.Title']"})
        },
        'staff.student': {
            'Meta': {'object_name': 'Student'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'people': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['staff.People']", 'unique': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'student_code': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'staff.title': {
            'Meta': {'object_name': 'Title'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['academic']