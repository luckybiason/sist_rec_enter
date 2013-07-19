#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from basiccrud.views import *

urlpatterns = patterns('usuario', 
    ## - Cadastro e listagem de usuarios
    url(r'^listagem/$',             'views.usuario_list',    name='usuario.listagem'),  
    url(r'^cadastro/$',             'views.usuario',         name='usuario.cadastro'),
    url(r'^cadastro/(?P<id>\d+)/$', 'views.usuario',         name='usuario.cadastro'),
    url(r'^detail/$',               'views.getdetail',       name='usuario.getdetail'),
    url(r'^recuperar_senha/$',      'views.recuperar_senha', name='usuario.recuperar_senha'),
    
    ## - Edição de listagem de permissões do usuário
    # a implementar futuramente
    #url(r'^permissoes/listagem/$',             'views.permissoes/_list', name='permissoes.listagem'),  
    #url(r'^permissoes/cadastro/$',             'views.permissoes/',      name='permissoes.cadastro'),
    #url(r'^permissoes/cadastro/(?P<id>\d+)/$', 'views.permissoes/',      name='permissoes.cadastro'),
)
    
