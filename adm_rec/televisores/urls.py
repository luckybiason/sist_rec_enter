#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import *
from basiccrud.views import *
from models import *

urlpatterns = patterns('televisores',            
                       
        ## - Cadastros auxiliares          
        # Tipos de telas
        url(r'^tipos_tela/listagem/$',             GeneralListView.as_view(model=TipoTela),   name='tipos_tela.listagem'),
        url(r'^tipos_tela/cadastro/$',             GeneralCreateView.as_view(model=TipoTela), name='tipos_tela.cadastro'),
        url(r'^tipos_tela/cadastro/(?P<pk>\d+)/$', GeneralUpdateView.as_view(model=TipoTela), name='tipos_tela.cadastro'),
        url(r'^tipos_tela/excluir/(?P<pk>\d+)/$',  GeneralDeleteView.as_view(model=TipoTela), name='tipos_tela.excluir'),
        # Funções
        url(r'^funcao/listagem/$',             GeneralListView.as_view(model=Funcao),   name='funcao.listagem'),
        url(r'^funcao/cadastro/$',             GeneralCreateView.as_view(model=Funcao), name='funcao.cadastro'),
        url(r'^funcao/cadastro/(?P<pk>\d+)/$', GeneralUpdateView.as_view(model=Funcao), name='funcao.cadastro'),
        url(r'^funcao/excluir/(?P<pk>\d+)/$',  GeneralDeleteView.as_view(model=Funcao), name='funcao.excluir'),
        # Modo preferencial de Imagem
        url(r'^modo_pref/listagem/$',             GeneralListView.as_view(model=ModoPref),   name='modo_pref.listagem'),
        url(r'^modo_pref/cadastro/$',             GeneralCreateView.as_view(model=ModoPref), name='modo_pref.cadastro'),
        url(r'^modo_pref/cadastro/(?P<pk>\d+)/$', GeneralUpdateView.as_view(model=ModoPref), name='modo_pref.cadastro'),
        url(r'^modo_pref/excluir/(?P<pk>\d+)/$',  GeneralDeleteView.as_view(model=ModoPref), name='modo_pref.excluir'),
        # Itens Inclusos
        url(r'^item/listagem/$',             GeneralListView.as_view(model=Item),   name='item.listagem'),
        url(r'^item/cadastro/$',             GeneralCreateView.as_view(model=Item), name='item.cadastro'),
        url(r'^item/cadastro/(?P<pk>\d+)/$', GeneralUpdateView.as_view(model=Item), name='item.cadastro'),
        url(r'^item/excluir/(?P<pk>\d+)/$',  GeneralDeleteView.as_view(model=Item), name='item.excluir'),
        # Entradas
        url(r'^entrada/listagem/$',             GeneralListView.as_view(model=Entrada),   name='entrada.listagem'),
        url(r'^entrada/cadastro/$',             GeneralCreateView.as_view(model=Entrada), name='entrada.cadastro'),
        url(r'^entrada/cadastro/(?P<pk>\d+)/$', GeneralUpdateView.as_view(model=Entrada), name='entrada.cadastro'),
        url(r'^entrada/excluir/(?P<pk>\d+)/$',  GeneralDeleteView.as_view(model=Entrada), name='entrada.excluir'),
        
)
