#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import *
from basiccrud.views import *
from models import *

urlpatterns = patterns('lojas',            
                       
        ## - Cadastro Loja
        url(r'^lojas/listagem/$',             GeneralListView.as_view(model=Loja),   name='lojas.listagem'),
        url(r'^lojas/cadastro/$',             GeneralCreateView.as_view(model=Loja, 
                                                                        template_name='lojas/cadastro.html'), name='lojas.cadastro'),
        url(r'^lojas/cadastro/(?P<pk>\d+)/$', GeneralUpdateView.as_view(model=Loja, 
                                                                        template_name='lojas/cadastro.html'), name='lojas.cadastro'),
        #url(r'^lojas/cadastro/$',             GeneralCreateView.as_view(model=Loja), name='lojas.cadastro'),
        #url(r'^lojas/cadastro/(?P<pk>\d+)/$', GeneralUpdateView.as_view(model=Loja), name='lojas.cadastro'),
        url(r'^lojas/excluir/(?P<pk>\d+)/$',  GeneralDeleteView.as_view(model=Loja), name='lojas.excluir'),
        
)
