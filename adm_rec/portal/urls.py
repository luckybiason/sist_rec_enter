#-*- coding: utf-8 -*-
from django.conf.urls          import patterns, include, url
from django.conf.urls.defaults import *
from django.conf               import settings


urlpatterns = patterns('portal.views',
    # Home
    url(r'^$', 'home',  name='portal.home'),
    url(r'^buscar$', 'buscar',  name='portal.buscar'),
    
)

# Configuração de urls de arquivos estáticos e de mídia
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
