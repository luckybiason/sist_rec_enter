#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf               import settings


urlpatterns = patterns('alerts_e_messages',
    url(r'^$', "views.show_alerts",  name='show_alerts'),
    
)