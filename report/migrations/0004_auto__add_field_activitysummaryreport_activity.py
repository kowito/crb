# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ActivitySummaryReport.activity'
        db.add_column('report_activitysummaryreport', 'activity',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['activity.Activity']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ActivitySummaryReport.activity'
        db.delete_column('report_activitysummaryreport', 'activity_id')


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
        'report.activityreport': {
            'Meta': {'object_name': 'ActivityReport'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['activity.Activity']"}),
            'attendance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['staff.Student']"}),
            'check_in': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'check_out': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'transaction_status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'version': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'report.activitysummaryreport': {
            'Meta': {'object_name': 'ActivitySummaryReport'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['activity.Activity']"}),
            'data': ('django.db.models.fields.TextField', [], {}),
            'generate_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.IntegerField', [], {}),
            'version': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
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

    complete_apps = ['report']