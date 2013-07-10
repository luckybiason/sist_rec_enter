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
                         'titulo'    : _(u"Vaga"),
                         'img'       : "img/grav.png",
                         'url-name'  : "vagas.listagem",
                         'id-html'   : "vaga",
                         'perm_need' : [''],
                     },
                     {  
                         'titulo'    : _(u"Cliente"),
                         'img'       : "img/users.png",
                         'url-name'  : "clientes.listagem",
                         'id-html'   : "cliente",
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
                                           'titulo'      : _(u"Auxiliares do Cliente"),
                                           'img'         : "img/icone_cadastro.gif",
                                           'id-html'     : "cadastrosauxcli",
                                           'itens-width' : "220",
                                           'perm_need'   : [''],
                                           'itens'  :[
                                                     { 
                                                         'titulo'    : _(u"Benefício"),
                                                         'img'       : "img/icone_cadastro.gif",
                                                         'url-name'  : "beneficio.listagem",
                                                         'id-html'   : "beneficio",
                                                         'perm_need' : [''],
                                                     },
                                                     { 
                                                         'titulo'    : _(u"Setor"),
                                                         'img'       : "img/icone_cadastro.gif",
                                                         'url-name'  : "setor.listagem",
                                                         'id-html'   : "setor",
                                                         'perm_need' : [''],
                                                     },
                                                      { 
                                                         'titulo'    : _(u"Ramo de Atividade"),
                                                         'img'       : "img/icone_cadastro.gif",
                                                         'url-name'  : "ramo.listagem",
                                                         'id-html'   : "ramo",
                                                         'perm_need' : [''],
                                                     },
                                           ]  # Fim itens submenu Cadastros Auxiliares do Cliente
                                     },  # Fim submenu Cadastros Auxiliares do Cliente
                                     { 
                                           'titulo'      : _(u"Auxiliares da Vaga"),
                                           'img'         : "img/icone_cadastro.gif",
                                           'id-html'     : "cadastrosauxcli",
                                           'itens-width' : "220",
                                           'perm_need'   : [''],
                                           'itens'  :[
                                                      { 
                                                         'titulo'    : _(u"Motivo de Manutenção de Vaga"),
                                                         'img'       : "img/icone_cadastro.gif",
                                                         'url-name'  : "motcancel.listagem",
                                                         'id-html'   : "motcancel",
                                                         'perm_need' : [''],
                                                     },
                
                                                     {  
                                                         'titulo'   : _(u"Motivo de Abertura"),
                                                         'img'      : "img/icone_cadastro.gif",
                                                         'url-name' : "motiv_aberturas.listagem",
                                                         'perm_need': [''],
                                                     },
                                           ]  # Fim itens submenu Cadastros Auxiliares da Vaga
                                     },  # Fim submenu Cadastros Auxiliares da Vaga
                                      { 
                                         'titulo'    : _(u"Conceito de Candidato"),
                                         'img'       : "img/icone_cadastro.gif",
                                         'url-name'  : "conceito_cand.listagem",
                                         'id-html'   : "conceito_cand",
                                         'perm_need' : [''],
                                     },

                                     {  
                                         'titulo'   : _(u"Funções"),
                                         'img'      : "img/icone_cadastro.gif",
                                         'url-name' : "funcoes.listagem",
                                         'perm_need': [''],
                                     },
                                     {  
                                         'titulo'   : _(u"Nível de Experiência"),
                                         'img'      : "img/icone_cadastro.gif",
                                         'url-name' : "nivel_exp.listagem",
                                         'perm_need': [''],
                                     },
                                     {  
                                         'titulo'   : _(u"Escolaridade"),
                                         'img'      : "img/icone_cadastro.gif",
                                         'url-name' : "escolaridades.listagem",
                                         'perm_need': [''],
                                     },
                                     { 
                                         'titulo'    : _(u"Religião"),
                                         'img'       : "img/icone_cadastro.gif",
                                         'url-name'  : "religiao.listagem",
                                         'id-html'   : "religiao",
                                         'perm_need' : [''],
                                     },

                           ]  # Fim itens submenu Cadastros Auxiliares
                     },  # Fim submenu Cadastros Auxiliares
           ]  # Fim itens
        },  # Fim submenu cadastros
              
        {  # Submenu Configurações
           'titulo'      : _(u"Configurações"),
           'img'         : "img/icone_cadastro.gif",
           'id-html'     : "config",
           'itens-width' : "110",
           'perm_need'   : [''],
           'itens'  :[
                     {  
                         'titulo'   : _(u"Temas"),
                         'img'      : "img/icone_cadastro.gif",
                         'url-name' : "themes.listar",
                         'perm_need'   : [''],
                     },
           ]  # Fim itens
        },  # Fim submenu cadastros
              
        {  # Submenu Testes
           'titulo'      : _(u"Testes"),
           'img'         : "img/icone_cadastro.gif",
           'id-html'     : "config",
           'itens-width' : "150",
           'perm_need'   : [''],
           'itens'  :[
                     {  
                         'titulo'   : _(u"Alertas e Mensagens"),
                         'img'      : "img/icone_cadastro.gif",
                         'url-name' : "show_alerts",
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
