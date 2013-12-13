# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pixel'
        db.create_table(u'django_pixel_pixel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('affiliate_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('pixel', self.gf('sanitizer.models.SanitizedTextField')(max_length=255)),
        ))
        db.send_create_signal(u'django_pixel', ['Pixel'])


    def backwards(self, orm):
        # Deleting model 'Pixel'
        db.delete_table(u'django_pixel_pixel')


    models = {
        u'django_pixel.pixel': {
            'Meta': {'object_name': 'Pixel'},
            'affiliate_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pixel': ('sanitizer.models.SanitizedTextField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['django_pixel']