#-*- coding: utf-8 -*-
from django.conf.urls          import patterns, include, url
from django.conf.urls.defaults import *
from django.conf               import settings


urlpatterns = patterns('portal.views',
    # Home
    url(r'^$',       'home',     name='portal.home'),
)
