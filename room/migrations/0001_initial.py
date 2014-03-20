# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Building'
        db.create_table('room_building', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('room', ['Building'])

        # Adding model 'Floor'
        db.create_table('room_floor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('building', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['room.Building'])),
        ))
        db.send_create_signal('room', ['Floor'])

        # Adding model 'Device'
        db.create_table('room_device', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('device_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('fac_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('room', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['room.Room'], null=True, blank=True)),
        ))
        db.send_create_signal('room', ['Device'])

        # Adding model 'Room'
        db.create_table('room_room', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('floor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['room.Floor'])),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('room', ['Room'])


    def backwards(self, orm):
        # Deleting model 'Building'
        db.delete_table('room_building')

        # Deleting model 'Floor'
        db.delete_table('room_floor')

        # Deleting model 'Device'
        db.delete_table('room_device')

        # Deleting model 'Room'
        db.delete_table('room_room')


    models = {
        'room.building': {
            'Meta': {'object_name': 'Building'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'room.device': {
            'Meta': {'object_name': 'Device'},
            'device_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'fac_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['room.Room']", 'null': 'True', 'blank': 'True'}),
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
        }
    }

    complete_apps = ['room']