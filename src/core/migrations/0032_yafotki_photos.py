# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."

        images = (
            (2, 'http://img-fotki.yandex.ru/get/6205/19044756.f8/0_82eb1_8a2e5839_orig'),
            (3, 'http://img-fotki.yandex.ru/get/6205/19044756.f8/0_82eb2_6ec83d48_orig'),
            (5, 'http://img-fotki.yandex.ru/get/6205/19044756.f8/0_82eb3_478180e8_orig'),
            (6, 'http://img-fotki.yandex.ru/get/6205/19044756.f8/0_82eb4_234a4c50_orig'),
            (7, 'http://img-fotki.yandex.ru/get/6104/19044756.f8/0_82eb5_6fc36c78_orig'),
            (8, 'http://img-fotki.yandex.ru/get/6205/19044756.f9/0_82eb6_15e570f4_orig'),
            (9, 'http://img-fotki.yandex.ru/get/6104/19044756.f9/0_82eb7_5dcf0a12_orig'),
            (10, 'http://img-fotki.yandex.ru/get/6205/19044756.f9/0_82eb8_6a698b55_orig'),
            (11, 'http://img-fotki.yandex.ru/get/6104/19044756.f9/0_82eb9_a6db3148_orig'),
            (12, 'http://img-fotki.yandex.ru/get/6204/19044756.f9/0_82eba_dcbd7acf_orig'),
            (13, 'http://img-fotki.yandex.ru/get/6104/19044756.f9/0_82ebb_d8d74c8c_orig'),
            (14, 'http://img-fotki.yandex.ru/get/5908/19044756.f9/0_82ebc_81b0466a_orig'),
            (19, 'http://img-fotki.yandex.ru/get/5907/19044756.f9/0_82ebd_c6ce023_orig'),
            (20, 'http://img-fotki.yandex.ru/get/6204/19044756.f9/0_82ebe_9ed6c6a3_orig'),
            (21, 'http://img-fotki.yandex.ru/get/5907/19044756.f9/0_82ebf_623ada70_orig'),
            (24, 'http://img-fotki.yandex.ru/get/6205/19044756.f9/0_82ec0_91bdb0cb_orig'),
            (25, 'http://img-fotki.yandex.ru/get/5908/19044756.f9/0_82ec1_8cfc5649_orig'),
            (26, 'http://img-fotki.yandex.ru/get/6104/19044756.f9/0_82ec2_974378aa_orig'),
            (27, 'http://img-fotki.yandex.ru/get/5907/19044756.f9/0_82ec3_fb26afb_orig'),
            (28, 'http://img-fotki.yandex.ru/get/5908/19044756.f9/0_82ec4_579f759b_orig'),
            (29, 'http://img-fotki.yandex.ru/get/6204/19044756.f9/0_82ec5_263c016d_orig'),
            (30, 'http://img-fotki.yandex.ru/get/6105/19044756.f9/0_82ec6_fc6b95d3_orig'),
            (31, 'http://img-fotki.yandex.ru/get/6104/19044756.f9/0_82ec7_6ace3027_orig'),
            (32, 'http://img-fotki.yandex.ru/get/5908/19044756.f9/0_82ec8_35c194b8_orig'),
            (33, 'http://img-fotki.yandex.ru/get/6105/19044756.f9/0_82ec9_a8eeb909_orig'),
            (34, 'http://img-fotki.yandex.ru/get/6104/19044756.f9/0_82eca_481da1ad_orig'),
            (35, 'http://img-fotki.yandex.ru/get/5908/19044756.f9/0_82ecb_420c1990_orig'),
            (36, 'http://img-fotki.yandex.ru/get/6105/19044756.f9/0_82ecc_81acc855_orig'),
            (37, 'http://img-fotki.yandex.ru/get/5907/19044756.f9/0_82ecd_93f56edf_orig'),
            (38, 'http://img-fotki.yandex.ru/get/6205/19044756.f9/0_82ece_b6c7a945_orig'),
            (39, 'http://img-fotki.yandex.ru/get/5908/19044756.f9/0_82ecf_f4c2d9ab_orig'),
            (40, 'http://img-fotki.yandex.ru/get/6104/19044756.f9/0_82ed0_3389c36e_orig'),
            (41, 'http://img-fotki.yandex.ru/get/5908/19044756.f9/0_82ed1_9b594462_orig'),
            (42, 'http://img-fotki.yandex.ru/get/6204/19044756.f9/0_82ed2_7280b5a_orig'),
            (43, 'http://img-fotki.yandex.ru/get/5908/19044756.f9/0_82ed3_9a7d4f4d_orig'),
            (44, 'http://img-fotki.yandex.ru/get/5908/19044756.f9/0_82ed4_9d4b2858_orig'),
            (45, 'http://img-fotki.yandex.ru/get/6205/19044756.f9/0_82ed5_f6e07a66_orig'),
            (46, 'http://img-fotki.yandex.ru/get/6105/19044756.f9/0_82ed6_970c85c4_orig'),
            (47, 'http://img-fotki.yandex.ru/get/6105/19044756.f9/0_82ed7_8f721288_orig'),
            (48, 'http://img-fotki.yandex.ru/get/5907/19044756.f9/0_82ed8_169f9d91_orig'),
            (49, 'http://img-fotki.yandex.ru/get/6204/19044756.f9/0_82ed9_382efa58_orig'),
            (50, 'http://img-fotki.yandex.ru/get/6204/19044756.f9/0_82eda_86e4eac9_orig'),
            (51, 'http://img-fotki.yandex.ru/get/6105/19044756.f9/0_82edb_4e46868a_orig'),
            (52, 'http://img-fotki.yandex.ru/get/6205/19044756.f9/0_82edc_913a65cb_orig'),
            (53, 'http://img-fotki.yandex.ru/get/6205/19044756.f9/0_82edd_e2015e9d_orig'),
            (54, 'http://img-fotki.yandex.ru/get/6204/19044756.f9/0_82ede_bb950688_orig'),
            (55, 'http://img-fotki.yandex.ru/get/6104/19044756.f9/0_82edf_a7b4ef11_orig'),
            (56, 'http://img-fotki.yandex.ru/get/5908/19044756.f9/0_82ee0_7962fe44_orig'),
            (57, 'http://img-fotki.yandex.ru/get/5908/19044756.f9/0_82ee1_7918c259_orig'),
            (58, 'http://img-fotki.yandex.ru/get/5907/19044756.f9/0_82ee2_306cfe20_orig'),
            (59, 'http://img-fotki.yandex.ru/get/5908/19044756.f9/0_82ee3_570beeac_orig'),
            (60, 'http://img-fotki.yandex.ru/get/6204/19044756.f9/0_82ee4_43705c95_orig'),
            (61, 'http://img-fotki.yandex.ru/get/6205/19044756.f9/0_82ee5_5d7a10f6_orig'),
            (62, 'http://img-fotki.yandex.ru/get/6104/19044756.f9/0_82ee6_487459c_orig'),
            (63, 'http://img-fotki.yandex.ru/get/6204/19044756.f9/0_82ee7_7ffe9078_orig'),
            (64, 'http://img-fotki.yandex.ru/get/5908/19044756.fa/0_82ee8_77f0486e_orig'),
            (65, 'http://img-fotki.yandex.ru/get/6205/19044756.fa/0_82ee9_aea006e2_orig'),
            (66, 'http://img-fotki.yandex.ru/get/6104/19044756.fa/0_82eea_d354189c_orig'),
            (67, 'http://img-fotki.yandex.ru/get/6205/19044756.fa/0_82eeb_f610dd86_orig'),
            (68, 'http://img-fotki.yandex.ru/get/6205/19044756.fa/0_82eec_30005b79_orig'),
            (69, 'http://img-fotki.yandex.ru/get/6104/19044756.fa/0_82eed_b46880ec_orig'),
            (70, 'http://img-fotki.yandex.ru/get/5908/19044756.fa/0_82eee_bc51c6b0_orig'),
            (71, 'http://img-fotki.yandex.ru/get/6104/19044756.fa/0_82eef_97a34db6_orig'),
            (72, 'http://img-fotki.yandex.ru/get/6205/19044756.fa/0_82ef0_9288bf18_orig'),
            (73, 'http://img-fotki.yandex.ru/get/6205/19044756.fa/0_82ef1_429a7746_orig'),
            (74, 'http://img-fotki.yandex.ru/get/5908/19044756.fa/0_82ef2_3977d2d_orig'),
            (75, 'http://img-fotki.yandex.ru/get/5907/19044756.fa/0_82ef3_7f7a9c44_orig'),
            (76, 'http://img-fotki.yandex.ru/get/6205/19044756.fa/0_82ef4_3880d271_orig'),
            (77, 'http://img-fotki.yandex.ru/get/5908/19044756.fa/0_82ef5_b2257575_orig'),
            (78, 'http://img-fotki.yandex.ru/get/6205/19044756.fa/0_82ef6_92ed8f00_orig'),
            (79, 'http://img-fotki.yandex.ru/get/6105/19044756.fa/0_82ef7_c5870803_orig'),
            (80, 'http://img-fotki.yandex.ru/get/6204/19044756.fa/0_82ef8_899dda08_orig'),
            (81, 'http://img-fotki.yandex.ru/get/6105/19044756.fa/0_82ef9_4a8b2b66_orig'),
            (82, 'http://img-fotki.yandex.ru/get/5908/19044756.fa/0_82efa_6bd1d2eb_orig'),
            (83, 'http://img-fotki.yandex.ru/get/6104/19044756.fa/0_82efb_31069be2_orig'),
            (84, 'http://img-fotki.yandex.ru/get/6205/19044756.fa/0_82efc_3c98d4f1_orig'),
        )

        for image in images:
            orm.Photo.objects.filter(pk=image[0]).update(img=image[1])

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
