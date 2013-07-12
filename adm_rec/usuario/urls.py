#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from basiccrud.views import *

urlpatterns = patterns('usuario', 
                       
    ## - Cadastro e listagem de usuarios
    url(r'^listagem/$',             'views.usuario_list', name='usuario.listagem'),  
    url(r'^cadastro/$',             'views.usuario',      name='usuario.cadastro'),
    url(r'^cadastro/(?P<id>\d+)/$', 'views.usuario',      name='usuario.cadastro'),
    url(r'^cadastro/(?P<id>\d+)/$', 'views.usuario',      name='usuario.cadastro'),
    # (desabilitada) url(r'^exclusao/(?P<id>\d+)/$', 'views.usuariodel', name='usuarios.excluir'),
    url(r'^detail/$',  'views.getdetail', name='usuario.getdetail'),
    
    ## - Edição de lisatgem de permissões do usuário
)
    
