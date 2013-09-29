#-*- coding: utf-8 -*-
from django.conf.urls          import patterns, include, url
from django.conf.urls.defaults import *
from django.conf               import settings


urlpatterns = patterns('importacao',
    url(r'^televisores/$', 'views.televisores_importacao',  name='importacao.televisores'),
)
