#-*- coding: utf-8 -*-
from django.conf.urls          import patterns, include, url
from django.conf.urls.defaults import *
from django.conf               import settings


urlpatterns = patterns('portal',
    # Home
    url(r'^$', 'views.home', name='portal.home'),
    # Produtos
    url(r'^visualizar/(?P<id_televisor>\d+)/$', 'views.visualizar',        name='portal.visualizar'),
    # Comentários
    url(r'^salvar_comentario/$', 'views.salvar_comentario', name='portal.salvar_comentario'), 
    url(r'^lista_comentarios/$', 'views.lista_comentarios', name='portal.lista_comentarios'),
)
