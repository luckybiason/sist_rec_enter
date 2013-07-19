# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('app_endereco.views',
    url(r'^carrega_cidades_do_estado/$', 'carrega_cidades_do_estado', name='endereco.carrega_cidades_do_estado'), # AJAX
    url(r'^get_nome_cidade/$',           'get_nome_cidade',           name='endereco.get_nome_cidade'),           # AJAX
)

