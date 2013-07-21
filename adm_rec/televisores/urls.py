#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import *
from basiccrud.views import *
from models import *

urlpatterns = patterns('televisores',            
                       
        ## - Cadastros auxiliares          
        # Marcas
        url(r'^marcas/listagem/$',             'views.marcas_listagem', name='marcas.listagem'),
        url(r'^marcas/cadastro/$',             'views.marcas_cadastro', name='marcas.cadastro'),
        url(r'^marcas/cadastro/(?P<pk>\d+)/$', 'views.marcas_editar',   name='marcas.cadastro'),
        url(r'^marcas/excluir/(?P<pk>\d+)/$',  'views.marcas_excluir',  name='marcas.excluir'),
        # Tipos de telas
        url(r'^tipos_tela/listagem/$',             'views.tipos_tela_listagem', name='tipos_tela.listagem'),
        url(r'^tipos_tela/cadastro/$',             'views.tipos_tela_cadastro', name='tipos_tela.cadastro'),
        url(r'^tipos_tela/cadastro/(?P<pk>\d+)/$', 'views.tipos_tela_editar',   name='tipos_tela.cadastro'),
        url(r'^tipos_tela/excluir/(?P<pk>\d+)/$',  'views.tipos_tela_excluir',  name='tipos_tela.excluir'),
        # Funções
        url(r'^funcao/listagem/$',             'views.funcao_listagem',  name='funcao.listagem'),
        url(r'^funcao/cadastro/$',             'views.funcao_cadastro',  name='funcao.cadastro'),
        url(r'^funcao/cadastro/(?P<pk>\d+)/$', 'views.funcao_editar',    name='funcao.cadastro'),
        url(r'^funcao/excluir/(?P<pk>\d+)/$',  'views.funcao_excluir',   name='funcao.excluir'),
        url(r'^funcao/detail/$',               'views.getdetail_funcao', name='funcao.getdetail'),
        # Modo preferencial de Imagem
        url(r'^modo_pref/listagem/$',             'views.modo_pref_listagem', name='modo_pref.listagem'),
        url(r'^modo_pref/cadastro/$',             'views.modo_pref_cadastro', name='modo_pref.cadastro'),
        url(r'^modo_pref/cadastro/(?P<pk>\d+)/$', 'views.modo_pref_editar',   name='modo_pref.cadastro'),
        url(r'^modo_pref/excluir/(?P<pk>\d+)/$',  'views.modo_pref_excluir',  name='modo_pref.excluir'),
        # Itens Inclusos
        url(r'^item/listagem/$',             'views.item_listagem', name='item.listagem'),
        url(r'^item/cadastro/$',             'views.item_cadastro', name='item.cadastro'),
        url(r'^item/cadastro/(?P<pk>\d+)/$', 'views.item_editar',   name='item.cadastro'),
        url(r'^item/excluir/(?P<pk>\d+)/$',  'views.item_excluir',  name='item.excluir'),
        # Entradas
        url(r'^entrada/listagem/$',             'views.entrada_listagem', name='entrada.listagem'),
        url(r'^entrada/cadastro/$',             'views.entrada_cadastro', name='entrada.cadastro'),
        url(r'^entrada/cadastro/(?P<pk>\d+)/$', 'views.entrada_editar',   name='entrada.cadastro'),
        url(r'^entrada/excluir/(?P<pk>\d+)/$',  'views.entrada_excluir',  name='entrada.excluir'),
        
        ## - Cadastros Principal        
        # Televisores
        url(r'^televisor/listagem/$',             'views.televisor_listagem',  name='televisor.listagem'),
        url(r'^televisor/cadastro/$',             'views.televisor_cadastro',  name='televisor.cadastro'),
        url(r'^televisor/cadastro/(?P<pk>\d+)/$', 'views.televisor_editar',    name='televisor.cadastro'),
        url(r'^televisor/excluir/(?P<pk>\d+)/$',  'views.televisor_excluir',   name='televisor.excluir'),
        url(r'^televisor/detail/$',               'views.getdetail_televisor', name='televisor.getdetail'),
        # Relacionamentos
        # - Conexões
        url(r'^conexoes/listagem/$',             'views.list_conexoes', name='conexoes.listagem'),
        url(r'^conexoes/cadastro/$',             'views.cad_conexoes',  name='conexoes.cadastro'),
        url(r'^conexoes/cadastro/(?P<pk>\d+)/$', 'views.cad_conexoes',  name='conexoes.cadastro'),
        url(r'^conexoes/excluir/(?P<pk>\d+)/$',  'views.exc_conexoes',  name='conexoes.excluir'),
        # - Itens inclusos
        url(r'^itens/listagem/$',             'views.list_itens', name='tel_itens.listagem'),
        url(r'^itens/cadastro/$',             'views.cad_itens',  name='tel_itens.cadastro'),
        url(r'^itens/cadastro/(?P<pk>\d+)/$', 'views.cad_itens',  name='tel_itens.cadastro'),
        url(r'^itens/excluir/(?P<pk>\d+)/$',  'views.exc_itens',  name='tel_itens.excluir'),
        # - Lojas
        url(r'^lojas/listagem/$',             'views.list_lojas', name='tel_lojas.listagem'),
        url(r'^lojas/cadastro/$',             'views.cad_lojas',  name='tel_lojas.cadastro'),
        url(r'^lojas/cadastro/(?P<pk>\d+)/$', 'views.cad_lojas',  name='tel_lojas.cadastro'),
        url(r'^lojas/excluir/(?P<pk>\d+)/$',  'views.exc_lojas',  name='tel_lojas.excluir'),
        
)
