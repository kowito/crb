# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Title'
        db.create_table('staff_title', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('staff', ['Title'])

        # Adding model 'FasUser'
        db.create_table(u'User', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gid', self.gf('django.db.models.fields.TextField')(db_column=u'GID')),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=16, db_column=u'UID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64, db_column=u'Name', blank=True)),
            ('utype', self.gf('django.db.models.fields.TextField')(db_column=u'UType')),
            ('securitylevel', self.gf('django.db.models.fields.TextField')(db_column=u'SecurityLevel')),
            ('finger1', self.gf('django.db.models.fields.CharField')(max_length=3, db_column=u'Finger1', blank=True)),
            ('template1', self.gf('django.db.models.fields.TextField')(db_column=u'Template1', blank=True)),
            ('finger2', self.gf('django.db.models.fields.CharField')(max_length=3, db_column=u'Finger2', blank=True)),
            ('template2', self.gf('django.db.models.fields.TextField')(db_column=u'Template2', blank=True)),
            ('finger3', self.gf('django.db.models.fields.CharField')(max_length=3, db_column=u'Finger3', blank=True)),
            ('template3', self.gf('django.db.models.fields.TextField')(db_column=u'Template3', blank=True)),
            ('admin', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'Admin')),
            ('suspend', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'Suspend')),
            ('password', self.gf('django.db.models.fields.TextField')(db_column=u'Password', blank=True)),
        ))
        db.send_create_signal('staff', ['FasUser'])

        # Adding model 'People'
        db.create_table('staff_people', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('title', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['staff.Title'])),
            ('name_th', self.gf('django.db.models.fields.CharField')(max_length=125, null=True)),
            ('lastname_th', self.gf('django.db.models.fields.CharField')(max_length=125, null=True)),
            ('name_eng', self.gf('django.db.models.fields.CharField')(max_length=125, null=True)),
            ('lastname_eng', self.gf('django.db.models.fields.CharField')(max_length=125, null=True)),
            ('citizen_id', self.gf('django.db.models.fields.CharField')(max_length=13, unique=True, null=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=125, null=True)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('staff', ['People'])

        # Adding model 'Student'
        db.create_table('staff_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('people', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['staff.People'], unique=True)),
            ('student_code', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('staff', ['Student'])

        # Adding model 'Instructor'
        db.create_table('staff_instructor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('people', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['staff.People'], unique=True)),
            ('employee_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal('staff', ['Instructor'])


    def backwards(self, orm):
        # Deleting model 'Title'
        db.delete_table('staff_title')

        # Deleting model 'FasUser'
        db.delete_table(u'User')

        # Deleting model 'People'
        db.delete_table('staff_people')

        # Deleting model 'Student'
        db.delete_table('staff_student')

        # Deleting model 'Instructor'
        db.delete_table('staff_instructor')


    models = {
        'staff.fasuser': {
            'Meta': {'object_name': 'FasUser', 'db_table': "u'User'"},
            'admin': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'Admin'"}),
            'finger1': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'Finger1'", 'blank': 'True'}),
            'finger2': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'Finger2'", 'blank': 'True'}),
            'finger3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'Finger3'", 'blank': 'True'}),
            'gid': ('django.db.models.fields.TextField', [], {'db_column': "u'GID'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_column': "u'Name'", 'blank': 'True'}),
            'password': ('django.db.models.fields.TextField', [], {'db_column': "u'Password'", 'blank': 'True'}),
            'securitylevel': ('django.db.models.fields.TextField', [], {'db_column': "u'SecurityLevel'"}),
            'suspend': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'Suspend'"}),
            'template1': ('django.db.models.fields.TextField', [], {'db_column': "u'Template1'", 'blank': 'True'}),
            'template2': ('django.db.models.fields.TextField', [], {'db_column': "u'Template2'", 'blank': 'True'}),
            'template3': ('django.db.models.fields.TextField', [], {'db_column': "u'Template3'", 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '16', 'db_column': "u'UID'"}),
            'utype': ('django.db.models.fields.TextField', [], {'db_column': "u'UType'"})
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

    complete_apps = ['staff']