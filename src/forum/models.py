# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse


class Thread(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"Заголовок")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=u"Дата создания")
    last_comment_date = models.DateTimeField(verbose_name=u"Дата последнего комментария")

    def __unicode__(self): return self.title

    def get_absolute_url(self):
        return reverse('forum_thread', args=[self.pk])

    class Meta:
        verbose_name = u"Тема"
        verbose_name_plural = u"Темы"
        ordering = ('-date_created',)


class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name=u"Автор")
    thread = models.ForeignKey(Thread, verbose_name=u"Тема")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=u"Дата создания")
    content = models.TextField(verbose_name=u"Содержимое")

    def __unicode__(self): return self.date_created

    class Meta:
        verbose_name = u"Комментарий"
        verbose_name_plural = u"Комментарии"
        ordering = ('-date_created',)