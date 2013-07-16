#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import *
from basiccrud.views import *
from models import *
from forms import *

urlpatterns = patterns('comp_visuais',            
                       
        ## - Cadastros auxiliares          
        # Categoria
        url(r'^categoria/listagem/$',             GeneralListView.as_view(model=Categoria),   name='categoria.listagem'),
        url(r'^categoria/cadastro/$',             GeneralCreateView.as_view(model=Categoria), name='categoria.cadastro'),
        url(r'^categoria/cadastro/(?P<pk>\d+)/$', GeneralUpdateView.as_view(model=Categoria), name='categoria.cadastro'),
        url(r'^categoria/excluir/(?P<pk>\d+)/$',  GeneralDeleteView.as_view(model=Categoria), name='categoria.excluir'),
                   
        ## - Cadastros Principal        
        # Componente Visual
        url(r'^comp_visuais/listagem/$',             GeneralListView.as_view(model=ComponenteVisual,
                                                                             with_details=True),   name='comp_visuais.listagem'),
        url(r'^comp_visuais/cadastro/$',             GeneralCreateView.as_view(model=ComponenteVisual, 
                                                                               template_name='comp_visuais/cadastro.html'), name='comp_visuais.cadastro'),
        url(r'^comp_visuais/cadastro/(?P<pk>\d+)/$', GeneralUpdateView.as_view(model=ComponenteVisual, 
                                                                               template_name='comp_visuais/cadastro.html'), name='comp_visuais.cadastro'),
        url(r'^comp_visuais/excluir/(?P<pk>\d+)/$',  GeneralDeleteView.as_view(model=ComponenteVisual), name='comp_visuais.excluir'),
        url(r'^comp_visuais/detail/$',  'views.getdetail_comp_visuais', name='comp_visuais.getdetail'),
)
