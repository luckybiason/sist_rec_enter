#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('filtragem',            
                       
        ## - Passos da filtragem
        url(r'^passo01/$', 'views.passo01', name='filtragem.passo01'),
        url(r'^passo02/$', 'views.passo02', name='filtragem.passo02'),
        url(r'^passo03/$', 'views.passo03', name='filtragem.passo03'),
        url(r'^passo04/$', 'views.passo04', name='filtragem.passo04'),
        url(r'^passo05/$', 'views.passo05', name='filtragem.passo05'),
        url(r'^passo06/$', 'views.passo06', name='filtragem.passo06'),
            
)
