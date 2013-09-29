# -*- coding: utf-8 -*-
# # Teste de Importação
from django.utils.translation import ugettext as _

MENU = lambda :{
    # # Configurações Globais
    'down_img': "img/arr_down.png",
    # # Itens
    'itens': [
              
        {  # Item de menu
            'titulo'    : _(u"Home"),
            'img'       : "img/home.png",
            'url'       : "/adm/",
            'perm_need' : [''],
        },
        {  # Submenu Cadastros
           'titulo'      : _(u"Cadastros"),
           'img'         : "img/default.png",
           'id-html'     : "cadastros",
           'itens-width' : "249",
           'perm_need'   : [''],
           'itens'  :[
                     { 
                         'titulo'    : _(u"Televisores"),
                         'img'       : "img/tele.png",
                         'url-name'  : "televisor.listagem",
                         'id-html'   : "televisores",
                         'perm_need' : [''],
                     },
                     {  
                         'titulo'    : _(u"Lojas"),
                         'img'       : "img/lojas.png",
                         'url-name'  : "lojas.listagem",
                         'id-html'   : "loja",
                         'perm_need' : [''],
                     },
                     { 
                           'titulo'      : _(u"Cadastros Auxiliares"),
                           'img'         : "img/cadas.png",
                           'id-html'     : "cadastrosaux",
                           'itens-width' : "280",
                           'perm_need'   : [''],
                           'itens'  :[
                                      { 
                                       'titulo'    : _(u"Marcas"),
                                       'img'       : "img/book.png",
                                       'url-name'  : "marcas.listagem",
                                       'id-html'   : "marcas",
                                       'perm_need' : [''],
                                       },
                                      { 
                                       'titulo'    : _(u"Entrada"),
                                       'img'       : "img/book.png",
                                       'url-name'  : "entrada.listagem",
                                       'id-html'   : "entrada",
                                       'perm_need' : [''],
                                       },
                                      { 
                                       'titulo'    : _(u"Funções"),
                                       'img'       : "img/book.png",
                                       'url-name'  : "funcao.listagem",
                                       'id-html'   : "funcao",
                                       'perm_need' : [''],
                                       },
                                      { 
                                       'titulo'    : _(u"Itens inclusos"),
                                       'img'       : "img/book.png",
                                       'url-name'  : "item.listagem",
                                       'id-html'   : "item",
                                       'perm_need' : [''],
                                       },
                                      { 
                                       'titulo'    : _(u"Modo preferencial de imagem"),
                                       'img'       : "img/book.png",
                                       'url-name'  : "modo_pref.listagem",
                                       'id-html'   : "modo_pref",
                                       'perm_need' : [''],
                                       },
                                      { 
                                       'titulo'    : _(u"Tipo de Tela"),
                                       'img'       : "img/book.png",
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
           'img'         : "img/settings.png",
           'id-html'     : "config",
           'itens-width' : "145",
           'perm_need'   : [''],
           'itens'  :[
                     {  
                         'titulo'   : _(u"Perfil de usuário"),
                         'img'      : "imagem/user_img.png",
                         'url-name' : "usuario.listagem",
                         'perm_need'   : [''],
                     },
                     {  
                         'titulo'   : _(u"Propagandas"),
                         'img'      : "img/users.png",
                         'url-name' : "propagandas.listagem",
                         'perm_need'   : [''],
                     },
                     {  
                         'titulo'   : _(u"Importar Televisores"),
                         'img'      : "img/tele.png",
                         'url-name' : "importacao.televisores",
                         'perm_need'   : [''],
                     },
           ]  # Fim itens
        },  # Fim submenu cadastros
        {  # Item de menu
            'titulo'    : _(u"Logout"),
            'img'       : "img/logout.png",
            'url'       : "/adm/logout/",
            'perm_need' : [''],
        },
    ]  # Fim MENU["itens"]
}  # Fim MENU
