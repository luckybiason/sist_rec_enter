#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from basiccrud.views import *

urlpatterns = patterns('usuario', 
    ## - Cadastro e listagem de usuarios
    url(r'^listagem/$',             'views.usuario_list',    name='usuario.listagem'),  
    url(r'^cadastro/$',             'views.usuario',         name='usuario.cadastro'),
    url(r'^cadastro/(?P<id>\d+)/$', 'views.usuario',         name='usuario.cadastro'),
    url(r'^recuperar_senha/$',      'views.recuperar_senha', name='usuario.recuperar_senha'),
    
)
    
