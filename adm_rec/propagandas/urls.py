#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import *
from basiccrud.views import *
from models import *

urlpatterns = patterns('propagandas',            
                       
        ## - Propagandas
        url(r'^propagandas/listagem/$',             'views.propagandas_listagem', name='propagandas.listagem'),
        url(r'^propagandas/cadastro/$',             'views.propagandas_cadastro', name='propagandas.cadastro'),
        url(r'^propagandas/cadastro/(?P<pk>\d+)/$', 'views.propagandas_editar',   name='propagandas.cadastro'),
        url(r'^propagandas/excluir/(?P<pk>\d+)/$',  'views.propagandas_excluir',  name='propagandas.excluir'),
        
)
