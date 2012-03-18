# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

from views import thread, edit_comment, index

urlpatterns = patterns('',    

    url(r'^thread/(\d+)', thread, name='forum_thread'),
    url(r'^edit/(\d+)', edit_comment, name='forum_edit_comment'),

    url(r'^$', index , name='forum_index'),
    )