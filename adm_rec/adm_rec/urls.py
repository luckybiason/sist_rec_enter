#-*- coding: utf-8 -*-
from django.conf.urls          import patterns, include, url
from django.conf.urls.defaults import *
from django.conf               import settings


urlpatterns = patterns('',
    ##### - Sistema administrador - #####
    url(r'^adm/$',       'adm_rec.views.menu',  name='menu'),
    
    # Sistema Login
    (r'^adm/login/$'  ,'django.contrib.auth.views.login',             {'template_name':'login.html'}),
    (r'^adm/logout/$' ,'django.contrib.auth.views.logout_then_login', {'login_url'    :'/login/'}),
    
    # Sistema de mensagens
    (r'adm/alerts_e_messages/',  include('alerts_e_messages.urls')),
    
    # Model de Dados
    (r'^adm/usuario/',     include('usuario.urls')),
    (r'^adm/lojas/',       include('lojas.urls')),
    (r'^adm/televisores/', include('televisores.urls')),
    (r'^adm/propagandas/', include('propagandas.urls')),
    (r'^clientes/',        include('clientes.urls')),
    
    # Processos
    (r'^adm/importacao/',     include('importacao.urls')),
    
    
    ##### - Portal - #####
    url(r'^$',       'adm_rec.views.portal',  name='portal'),
    (r'^portal/',    include('portal.urls')),
    (r'^buscar/',    include('busca.urls')),
    (r'^filtragem/', include('filtragem.urls')),
)

# Configuração de urls de arquivos estáticos e de mídia
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
