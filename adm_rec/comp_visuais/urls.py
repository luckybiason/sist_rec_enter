#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import *
from basiccrud.views import *
from models import *

urlpatterns = patterns('comp_visuais',            
                       
        ## - Cadastros auxiliares          
        # Categoria
        url(r'^categoria/listagem/$',             GeneralListView.as_view(model=Categoria),   name='categoria.listagem'),
        url(r'^categoria/cadastro/$',             GeneralCreateView.as_view(model=Categoria), name='categoria.cadastro'),
        url(r'^categoria/cadastro/(?P<pk>\d+)/$', GeneralUpdateView.as_view(model=Categoria), name='categoria.cadastro'),
        url(r'^categoria/excluir/(?P<pk>\d+)/$',  GeneralDeleteView.as_view(model=Categoria), name='categoria.excluir'),
        
)
