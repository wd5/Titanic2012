# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."

        images = (
            (1, 'http://img-fotki.yandex.ru/get/6204/19044756.f8/0_82e87_ad55a5d8_orig'),
            (2, 'http://img-fotki.yandex.ru/get/6204/19044756.f8/0_82e85_6f9d780d_orig'),
            (3, 'http://img-fotki.yandex.ru/get/5908/19044756.f8/0_82e84_343a3655_orig'),
            (4, 'http://img-fotki.yandex.ru/get/6104/19044756.f8/0_82e83_1ed6706d_orig'),
            (5, 'http://img-fotki.yandex.ru/get/6104/19044756.f8/0_82e82_574f0a78_orig'),
            (6, 'http://img-fotki.yandex.ru/get/6105/19044756.f8/0_82e81_da2c7e73_orig'),
            (7, 'http://img-fotki.yandex.ru/get/5908/19044756.f8/0_82e80_4a39d2f7_orig'),
            (8, 'http://img-fotki.yandex.ru/get/6104/19044756.f8/0_82e7f_aea1d59d_orig'),
            (10, 'http://img-fotki.yandex.ru/get/6104/19044756.f8/0_82e7e_d404ef1a_orig'),
            (11, 'http://img-fotki.yandex.ru/get/6104/19044756.f8/0_82e7d_7e6a9e4_orig'),
            (12, 'http://img-fotki.yandex.ru/get/5908/19044756.f8/0_82e7c_f1ed6e28_orig'),
            (13, 'http://img-fotki.yandex.ru/get/5907/19044756.f8/0_82e7b_fe24ff7e_orig'),
            (14, 'http://img-fotki.yandex.ru/get/6204/19044756.f8/0_82e7a_1abc0bcd_orig'),
            (15, 'http://img-fotki.yandex.ru/get/6104/19044756.f7/0_82e79_4b1919aa_orig'),
            (16, 'http://img-fotki.yandex.ru/get/6204/19044756.f7/0_82e78_398c5b35_orig'),
            (17, 'http://img-fotki.yandex.ru/get/6104/19044756.f7/0_82e77_473ab4c2_orig'),
            (18, 'http://img-fotki.yandex.ru/get/5908/19044756.f7/0_82e76_6620f36f_orig'),
            (19, 'http://img-fotki.yandex.ru/get/6205/19044756.f7/0_82e75_625e0fb2_orig'),
            (20, 'http://img-fotki.yandex.ru/get/5908/19044756.f7/0_82e74_35f7e5a8_orig'),
            (22, 'http://img-fotki.yandex.ru/get/6205/19044756.f7/0_82e73_8012e69b_orig'),
            (23, 'http://img-fotki.yandex.ru/get/6204/19044756.f7/0_82e72_2446e125_orig'),
            (24, 'http://img-fotki.yandex.ru/get/5908/19044756.f7/0_82e71_ef1dd87f_orig'),
            (25, 'http://img-fotki.yandex.ru/get/6205/19044756.f7/0_82e70_c9c2a391_orig'),
        )

        for image in images:
            orm.Post.objects.filter(pk=image[0]).update(img=image[1])



    def backwards(self, orm):
        "Write your backwards methods here."


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
    symmetrical = True
