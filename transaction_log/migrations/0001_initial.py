# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Transaction'
        db.create_table(u'RALog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column=u'RN')),
            ('gid', self.gf('django.db.models.fields.TextField')(db_column=u'GID', blank=True)),
            ('fid', self.gf('django.db.models.fields.TextField')(db_column=u'FID', blank=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=16, db_column=u'UID', blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64, db_column=u'Name', blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'Date', blank=True)),
            ('time', self.gf('django.db.models.fields.CharField')(max_length=16, db_column=u'Time', blank=True)),
            ('facid', self.gf('django.db.models.fields.TextField')(db_column=u'FacID', blank=True)),
            ('inoutoption', self.gf('django.db.models.fields.TextField')(db_column=u'InOutOption', blank=True)),
            ('other', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Other', blank=True)),
        ))
        db.send_create_signal('transaction_log', ['Transaction'])


    def backwards(self, orm):
        # Deleting model 'Transaction'
        db.delete_table(u'RALog')


    models = {
        'transaction_log.transaction': {
            'Meta': {'ordering': "['-timestamp']", 'object_name': 'Transaction', 'db_table': "u'RALog'"},
            'facid': ('django.db.models.fields.TextField', [], {'db_column': "u'FacID'", 'blank': 'True'}),
            'fid': ('django.db.models.fields.TextField', [], {'db_column': "u'FID'", 'blank': 'True'}),
            'gid': ('django.db.models.fields.TextField', [], {'db_column': "u'GID'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'RN'"}),
            'inoutoption': ('django.db.models.fields.TextField', [], {'db_column': "u'InOutOption'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_column': "u'Name'", 'blank': 'True'}),
            'other': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Other'", 'blank': 'True'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '16', 'db_column': "u'Time'", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'Date'", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '16', 'db_column': "u'UID'", 'blank': 'True'})
        }
    }

    complete_apps = ['transaction_log']