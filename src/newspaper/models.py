# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

from yafotki.fields import YFField

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^yafotki\.fields\.YFField"])


class Post(models.Model):
    NEWSPAPER = (
        (1, u'The Times'),
        (2, u'The Economist'),
        (3, u'Manchester Guardian'),
        (4, u'NewYork Post'),
    )
    newspaper = models.IntegerField(choices=NEWSPAPER, default=1, verbose_name=u"Газета")
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, verbose_name=u"Заголовок")
    image = models.ImageField(upload_to='data', verbose_name=u"Картинка")
    img = YFField(
        verbose_name=u"Фото",
        upload_to='titanic',
        null=True, blank=True, default=None,
    )

    content = models.TextField(verbose_name=u"Содержание")

    def __unicode__(self):
        return u"%s: %s" % (self.get_newspaper_display(), self.title)

    def get_absolute_url(self):
        return reverse('post', args=[self.pk])

    class Meta:
        verbose_name = u"Выпуск"
        verbose_name_plural = u"Выпуски"
        ordering = ('-date_created',)
