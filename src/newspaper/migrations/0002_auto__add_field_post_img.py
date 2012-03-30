# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.img'
        db.add_column('newspaper_post', 'img',
                      self.gf('yafotki.fields.YFField')(default=None, max_length=255, null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Post.img'
        db.delete_column('newspaper_post', 'img')

    models = {
        'newspaper.post': {
            'Meta': {'ordering': "('-date_created',)", 'object_name': 'Post'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'img': ('yafotki.fields.YFField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'newspaper': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['newspaper']
