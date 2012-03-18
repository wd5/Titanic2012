# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Role'
        db.create_table('core_role', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ticket_level', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('profession', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sex', self.gf('django.db.models.fields.CharField')(default='m', max_length=1)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=10000)),
        ))
        db.send_create_signal('core', ['Role'])

        # Adding model 'Profile'
        db.create_table('core_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nick', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('icq', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('tel', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('med', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('money_total', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ticket_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('money_cafe', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('money_casino', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('wsl_actions', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('gl_actions', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('money_cache', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('gun', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('goal', self.gf('django.db.models.fields.TextField')()),
            ('dream', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Role'], null=True, blank=True)),
        ))
        db.send_create_signal('core', ['Profile'])


    def backwards(self, orm):
        
        # Deleting model 'Role'
        db.delete_table('core_role')

        # Deleting model 'Profile'
        db.delete_table('core_profile')


    models = {
        'core.profile': {
            'Meta': {'object_name': 'Profile'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'dream': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'gl_actions': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'goal': ('django.db.models.fields.TextField', [], {}),
            'gun': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'icq': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'med': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'money_cache': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'money_cafe': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'money_casino': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'money_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nick': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Role']", 'null': 'True', 'blank': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ticket_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'wsl_actions': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'core.role': {
            'Meta': {'object_name': 'Role'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10000'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'m'", 'max_length': '1'}),
            'ticket_level': ('django.db.models.fields.IntegerField', [], {'default': '5'})
        }
    }

    complete_apps = ['core']
