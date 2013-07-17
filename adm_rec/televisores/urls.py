#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import *
from basiccrud.views import *
from models import *

urlpatterns = patterns('televisores',            
                       
        ## - Cadastros auxiliares          
        # Marcas
        url(r'^marcas/listagem/$',             GeneralListView.as_view(model=Marca),   name='marcas.listagem'),
        url(r'^marcas/cadastro/$',             GeneralCreateView.as_view(model=Marca), name='marcas.cadastro'),
        url(r'^marcas/cadastro/(?P<pk>\d+)/$', GeneralUpdateView.as_view(model=Marca), name='marcas.cadastro'),
        url(r'^marcas/excluir/(?P<pk>\d+)/$',  GeneralDeleteView.as_view(model=Marca), name='marcas.excluir'),
        # Tipos de telas
        url(r'^tipos_tela/listagem/$',             GeneralListView.as_view(model=TipoTela),   name='tipos_tela.listagem'),
        url(r'^tipos_tela/cadastro/$',             GeneralCreateView.as_view(model=TipoTela), name='tipos_tela.cadastro'),
        url(r'^tipos_tela/cadastro/(?P<pk>\d+)/$', GeneralUpdateView.as_view(model=TipoTela), name='tipos_tela.cadastro'),
        url(r'^tipos_tela/excluir/(?P<pk>\d+)/$',  GeneralDeleteView.as_view(model=TipoTela), name='tipos_tela.excluir'),
        # Funções
        url(r'^funcao/listagem/$',             GeneralListView.as_view(model=Funcao, with_details=True), name='funcao.listagem'),
        url(r'^funcao/cadastro/$',             GeneralCreateView.as_view(model=Funcao), name='funcao.cadastro'),
        url(r'^funcao/cadastro/(?P<pk>\d+)/$', GeneralUpdateView.as_view(model=Funcao), name='funcao.cadastro'),
        url(r'^funcao/excluir/(?P<pk>\d+)/$',  GeneralDeleteView.as_view(model=Funcao), name='funcao.excluir'),
        url(r'^funcao/detail/$',               'views.getdetail_funcao',                name='funcao.getdetail'),
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
        
        ## - Cadastros Principal        
        # Televisores
        url(r'^televisor/listagem/$',             GeneralListView.as_view(model=Televisor, with_details=True), name='televisor.listagem'),
        url(r'^televisor/cadastro/$',             'views.cad_televisor', name='televisor.cadastro'),
        url(r'^televisor/cadastro/(?P<pk>\d+)/$', 'views.upd_televisor', name='televisor.cadastro'),
        url(r'^televisor/excluir/(?P<pk>\d+)/$',  GeneralDeleteView.as_view(model=Televisor), name='televisor.excluir'),
        url(r'^televisor/detail/$',  'views.getdetail_televisor', name='televisor.getdetail'),
)
