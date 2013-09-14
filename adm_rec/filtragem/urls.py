#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('filtragem',            
                       
        ## - Passos da filtragem
        url(r'^passo01/$', 'views.passo01', name='filtragem.passo01'),
        url(r'^passo02/$', 'views.passo02', name='filtragem.passo02'),
            
)
