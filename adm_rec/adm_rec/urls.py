#-*- coding: utf-8 -*-
from django.conf.urls          import patterns, include, url
from django.conf.urls.defaults import *
from django.conf               import settings


urlpatterns = patterns('',
    # Menu (Simples)
    url(r'^$',       'adm_rec.views.menu',  name='menu'),
    #url(r'^about/$', 'adm_rec.views.about', name='about'),
    
    # Sistema Login
    (r'^login/$'  ,'django.contrib.auth.views.login',             {'template_name':'login.html'}),
    (r'^logout/$' ,'django.contrib.auth.views.logout_then_login', {'login_url'    :'/login/'}),
      
    # Sistema de mensagens
    (r'alerts_e_messages/',  include('alerts_e_messages.urls')),
        
    # Captchas
    #(r'captchas/',  include('captchas.urls')),
    
    # Model de Dados
    (r'^usuario/',      include('usuario.urls')),
    (r'^lojas/',        include('lojas.urls')),
    (r'^televisores/',  include('televisores.urls')),
)

# Configuração de urls de arquivos estáticos e de mídia
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
