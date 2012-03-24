# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."

        images = (
            (5, 'http://img-fotki.yandex.ru/get/6104/19044756.f8/0_82e8d_a8aa3a94_orig'),
            (7, 'http://img-fotki.yandex.ru/get/6205/19044756.f8/0_82e8e_6244c253_orig'),
            (19, 'http://img-fotki.yandex.ru/get/6104/19044756.f8/0_82e92_dcaf2905_orig'),
            (31, 'http://img-fotki.yandex.ru/get/6204/19044756.f8/0_82e93_42a4f723_orig'),
            (41, 'http://img-fotki.yandex.ru/get/6104/19044756.f8/0_82e94_10d49ff1_orig'),
            (42, 'http://img-fotki.yandex.ru/get/5908/19044756.f8/0_82e95_b68653a5_orig'),
            (45, 'http://img-fotki.yandex.ru/get/6104/19044756.f8/0_82e96_c8ecee92_orig'),
            (46, 'http://img-fotki.yandex.ru/get/6105/19044756.f8/0_82e97_deac3760_orig'),
            (50, 'http://img-fotki.yandex.ru/get/6104/19044756.f8/0_82e98_678698eb_orig'),
            (53, 'http://img-fotki.yandex.ru/get/5907/19044756.f8/0_82e99_dda89f62_orig'),
            (54, 'http://img-fotki.yandex.ru/get/6105/19044756.f8/0_82e9a_ab2a9c97_orig'),
            (56, 'http://img-fotki.yandex.ru/get/5907/19044756.f8/0_82e9b_643f1ea6_orig'),
            (61, 'http://img-fotki.yandex.ru/get/6204/19044756.f8/0_82e9c_3e1a2228_orig'),
            (62, 'http://img-fotki.yandex.ru/get/6105/19044756.f8/0_82e9d_a23df8b2_orig'),
            (63, 'http://img-fotki.yandex.ru/get/5907/19044756.f8/0_82e9e_8be4a6ec_orig'),
            (64, 'http://img-fotki.yandex.ru/get/6105/19044756.f8/0_82e9f_29d2fd89_orig'),
            (76, 'http://img-fotki.yandex.ru/get/6205/19044756.f8/0_82ea0_62ff9638_orig'),
            (78, 'http://img-fotki.yandex.ru/get/5908/19044756.f8/0_82ea1_99841fff_orig'),
            (80, 'http://img-fotki.yandex.ru/get/6205/19044756.f8/0_82ea2_8f0ed8f8_orig'),
            (81, 'http://img-fotki.yandex.ru/get/6205/19044756.f8/0_82ea3_958f66ef_orig'),
            (83, 'http://img-fotki.yandex.ru/get/6105/19044756.f8/0_82ea4_53700da8_orig'),
            (88, 'http://img-fotki.yandex.ru/get/6105/19044756.f8/0_82ea5_ec446df7_orig'),
            (92, 'http://img-fotki.yandex.ru/get/6205/19044756.f8/0_82ea6_3d0e233e_orig'),
            (93, 'http://img-fotki.yandex.ru/get/5908/19044756.f8/0_82ea7_8155d50b_orig'),
            (94, 'http://img-fotki.yandex.ru/get/5908/19044756.f8/0_82ea8_702c5f3_orig'),
            (105, 'http://img-fotki.yandex.ru/get/6205/19044756.f8/0_82ea9_ab4f029f_orig'),
            (106, 'http://img-fotki.yandex.ru/get/5908/19044756.f8/0_82eaa_53982e3a_orig'),
            (109, 'http://img-fotki.yandex.ru/get/6104/19044756.f8/0_82eab_6cac79a0_orig'),
            (110, 'http://img-fotki.yandex.ru/get/6204/19044756.f8/0_82eac_e62ffafa_orig'),
            (116, 'http://img-fotki.yandex.ru/get/6205/19044756.f8/0_82ead_90463857_orig'),
        )

        for image in images:
            orm.Profile.objects.filter(pk=image[0]).update(portrait=image[1])


    def backwards(self, orm):
        "Write your backwards methods here."


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.dance': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Dance'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '100'}),
            'scheme': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'core.floor': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Floor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'\\u044d\\u0442\\u0430\\u0436'", 'max_length': '200'})
        },
        'core.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'core.layer': {
            'Meta': {'object_name': 'Layer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'core.layerconnection': {
            'Meta': {'object_name': 'LayerConnection'},
            'comment': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'layer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'roles'", 'to': "orm['core.Layer']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Role']"})
        },
        'core.news': {
            'Meta': {'ordering': "('-date_created',)", 'object_name': 'News'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'core.photo': {
            'Meta': {'object_name': 'Photo'},
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('core.models.ThumbnailImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'img': ('yafotki.fields.YFField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'core.profile': {
            'Meta': {'object_name': 'Profile'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'agreement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'dream': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'food': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gl_actions': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'goal': ('django.db.models.fields.TextField', [], {}),
            'gun': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'icq': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locked_fields': ('django.db.models.fields.CharField', [], {'max_length': "'300'", 'null': 'True', 'blank': 'True'}),
            'med': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'money_cache': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'money_cafe': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'money_casino': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'money_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'passport_number': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'passport_serial': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'photo': ('core.models.ThumbnailImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'portrait': ('yafotki.fields.YFField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quest': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'suggested_role'", 'null': 'True', 'to': "orm['core.Role']"}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['core.Room']", 'null': 'True', 'blank': 'True'}),
            'social_number': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'special': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'wsl_actions': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'core.role': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Role'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'cabin': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10000'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'locked_role'", 'null': 'True', 'to': "orm['core.Profile']"}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'m'", 'max_length': '1'}),
            'ticket_level': ('django.db.models.fields.IntegerField', [], {'default': '5'})
        },
        'core.roleconnection': {
            'Meta': {'object_name': 'RoleConnection'},
            'comment': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'roles'", 'to': "orm['core.Role']"}),
            'role_rel': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'linked_roles'", 'null': 'True', 'to': "orm['core.Role']"})
        },
        'core.room': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Room'},
            'capacity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2'}),
            'current': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'floor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Floor']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'-'", 'max_length': '200'})
        }
    }

    complete_apps = ['core']
    symmetrical = True
