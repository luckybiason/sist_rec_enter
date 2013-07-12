# -*- coding: utf-8 -*-
# # Teste de Importação
from django.utils.translation import ugettext as _

MENU = lambda :{
    # # Configurações Globais
    'down_img': "img/down.png",
    # # Itens
    'itens': [
        {  # Submenu Cadastros
           'titulo'      : _(u"Cadastros"),
           'img'         : "img/icone_cadastro.gif",
           'id-html'     : "cadastros",
           'itens-width' : "249",
           'perm_need'   : [''],
           'itens'  :[
                     { 
                         'titulo'    : _(u"Televisores"),
                         'img'       : "img/grav.png",
                         'url'  : "vagas.listagem",
                         'id-html'   : "televisores",
                         'perm_need' : [''],
                     },
                     {  
                         'titulo'    : _(u"Componentes Visuais"),
                         'img'       : "img/users.png",
                         'url'  : "clientes.listagem",
                         'id-html'   : "compo_visu",
                         'perm_need' : [''],
                     },
                     { 
                           'titulo'      : _(u"Cadastros Auxiliares"),
                           'img'         : "img/icone_cadastro.gif",
                           'id-html'     : "cadastrosaux",
                           'itens-width' : "280",
                           'perm_need'   : [''],
                           'itens'  :[
                                      { 
                                       'titulo'    : _(u"Categoria (Componente)"),
                                       'img'       : "img/icone_cadastro.gif",
                                       'url-name'  : "categoria.listagem",
                                       'id-html'   : "categoria",
                                       'perm_need' : [''],
                                       },
                                      { 
                                       'titulo'    : _(u"Entrada"),
                                       'img'       : "img/icone_cadastro.gif",
                                       'url-name'  : "entrada.listagem",
                                       'id-html'   : "entrada",
                                       'perm_need' : [''],
                                       },
                                      { 
                                       'titulo'    : _(u"Funções"),
                                       'img'       : "img/icone_cadastro.gif",
                                       'url-name'  : "funcao.listagem",
                                       'id-html'   : "funcao",
                                       'perm_need' : [''],
                                       },
                                      { 
                                       'titulo'    : _(u"Itens inclusos"),
                                       'img'       : "img/icone_cadastro.gif",
                                       'url-name'  : "item.listagem",
                                       'id-html'   : "item",
                                       'perm_need' : [''],
                                       },
                                      { 
                                       'titulo'    : _(u"Modo preferencial de imagem"),
                                       'img'       : "img/icone_cadastro.gif",
                                       'url-name'  : "modo_pref.listagem",
                                       'id-html'   : "modo_pref",
                                       'perm_need' : [''],
                                       },
                                      { 
                                       'titulo'    : _(u"Tipo de Tela"),
                                       'img'       : "img/icone_cadastro.gif",
                                       'url-name'  : "tipos_tela.listagem",
                                       'id-html'   : "tipo_tela",
                                       'perm_need' : [''],
                                       },
                                     

                           ]  # Fim itens submenu Cadastros Auxiliares
                     },  # Fim submenu Cadastros Auxiliares
           ]  # Fim itens
        },  # Fim submenu cadastros
              
        {  # Submenu Gerenciamento
           'titulo'      : _(u"Gerenciamento"),
           'img'         : "img/icone_cadastro.gif",
           'id-html'     : "config",
           'itens-width' : "145",
           'perm_need'   : [''],
           'itens'  :[
                     {  
                         'titulo'   : _(u"Perfil de usuário"),
                         'img'      : "img/icone_cadastro.gif",
                         'url-name' : "usuario.listagem",
                         'perm_need'   : [''],
                     },
           ]  # Fim itens
        },  # Fim submenu cadastros
              
        {  # Item de menu
            'titulo'    : _(u"Logout"),
            # 'img'       : "img/icone_cadastro.gif",
            'url'       : "/logout/",
            'perm_need' : [''],
        },
    ]  # Fim MENU["itens"]
}  # Fim MENU
