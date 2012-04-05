# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic import list_detail
from django.contrib.auth.views import password_reset

from views import *
from models import News, Dance

urlpatterns = patterns('',

    #url(r'^master/(\d+)', master, name='master'),
    #url(r'^administrator/(\d+)', administrator, name='administrator'),

    url(r'^roles$', roles, name='roles'),
    url(r'^form', request_form, name='form'),
    url(r'^lock$', lock, name='lock'),
    url(r'^lock_rel$', lock_rel, name='lock_rel'),
    url(r'^gallery/(\d+)', gallery, name='gallery'),
    url(r'^news$', list_detail.object_list, {"queryset": News.objects.all()}, name='news'),
    url(r'^dances$', list_detail.object_list, {"queryset": Dance.objects.all()}, name='dances'),
    url(r'^bus', bus, name='bus'),
    url(r'^food', food, name='food'),
    url(r'^rooms', rooms, name='rooms'),
    url(r'^agreement', agreement, name='agreement'),

    url(r'^reports/$', reports),
    url(r'^reports/actions/$', report_actions),
    url(r'^reports/money/$', report_money),
    url(r'^reports/contacts/$', report_contacts),
    url(r'^reports/paid/$', report_paid),
    url(r'^reports/layers/$', report_layers),
    url(r'^reports/players_without_roles/$', report_players_without_roles),
    url(r'^reports/agreements/$', report_agreements),
    url(r'^reports/captain/$', report_captain),
    url(r'^reports/bus/$', report_bus),
    url(r'^reports/cafe/$', report_cafe),
    url(r'^reports/casino/$', report_casino),
    url(r'^reports/base/$', report_base),
    url(r'^reports/pay/$', report_pay),

    url(r'^$', index, name='index'),
    )
