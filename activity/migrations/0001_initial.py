# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ActivityGroup'
        db.create_table('activity_activitygroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('academic_year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['academic.AcademicYear'])),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('repeat_day', self.gf('crb.utils.MultiSelectField')(max_length=100)),
            ('repeat_week', self.gf('crb.utils.MultiSelectField')(max_length=100)),
            ('late_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('miss_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('version', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('activity', ['ActivityGroup'])

        # Adding M2M table for field student on 'ActivityGroup'
        db.create_table('activity_activitygroup_student', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activitygroup', models.ForeignKey(orm['activity.activitygroup'], null=False)),
            ('student', models.ForeignKey(orm['staff.student'], null=False))
        ))
        db.create_unique('activity_activitygroup_student', ['activitygroup_id', 'student_id'])

        # Adding M2M table for field instructor on 'ActivityGroup'
        db.create_table('activity_activitygroup_instructor', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activitygroup', models.ForeignKey(orm['activity.activitygroup'], null=False)),
            ('instructor', models.ForeignKey(orm['staff.instructor'], null=False))
        ))
        db.create_unique('activity_activitygroup_instructor', ['activitygroup_id', 'instructor_id'])

        # Adding model 'Activity'
        db.create_table('activity_activity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=120, null=True, blank=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['activity.ActivityGroup'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('late_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('actually_start_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('miss_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('calcled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_report_generated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('stat_ok', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('stat_late', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('stat_miss', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('version', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('activity', ['Activity'])

        # Adding M2M table for field student on 'Activity'
        db.create_table('activity_activity_student', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activity', models.ForeignKey(orm['activity.activity'], null=False)),
            ('student', models.ForeignKey(orm['staff.student'], null=False))
        ))
        db.create_unique('activity_activity_student', ['activity_id', 'student_id'])

        # Adding M2M table for field instructor on 'Activity'
        db.create_table('activity_activity_instructor', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activity', models.ForeignKey(orm['activity.activity'], null=False)),
            ('instructor', models.ForeignKey(orm['staff.instructor'], null=False))
        ))
        db.create_unique('activity_activity_instructor', ['activity_id', 'instructor_id'])


    def backwards(self, orm):
        # Deleting model 'ActivityGroup'
        db.delete_table('activity_activitygroup')

        # Removing M2M table for field student on 'ActivityGroup'
        db.delete_table('activity_activitygroup_student')

        # Removing M2M table for field instructor on 'ActivityGroup'
        db.delete_table('activity_activitygroup_instructor')

        # Deleting model 'Activity'
        db.delete_table('activity_activity')

        # Removing M2M table for field student on 'Activity'
        db.delete_table('activity_activity_student')

        # Removing M2M table for field instructor on 'Activity'
        db.delete_table('activity_activity_instructor')


    models = {
        'academic.academicyear': {
            'Meta': {'object_name': 'AcademicYear'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'activity.activity': {
            'Meta': {'ordering': "['date']", 'object_name': 'Activity'},
            'actually_start_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'calcled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['activity.ActivityGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'activity_student'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['staff.Instructor']"}),
            'is_report_generated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'late_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'miss_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'stat_late': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'stat_miss': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'stat_ok': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'student': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'activity_student'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['staff.Student']"}),
            'version': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'activity.activitygroup': {
            'Meta': {'object_name': 'ActivityGroup'},
            'academic_year': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['academic.AcademicYear']"}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'activity_group_instructor'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['staff.Instructor']"}),
            'late_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'miss_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'repeat_day': ('crb.utils.MultiSelectField', [], {'max_length': '100'}),
            'repeat_week': ('crb.utils.MultiSelectField', [], {'max_length': '100'}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'student': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'activity_group_student'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['staff.Student']"}),
            'version': ('django.db.models.fields.IntegerField', [], {'default': '1'})
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

    complete_apps = ['activity']