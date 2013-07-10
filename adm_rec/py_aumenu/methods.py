#-*- coding: utf-8 -*-
from menu import MENU
from django.core.urlresolvers import reverse
from django.conf import settings

##########  - Variáveis Auxiliares

menu  = "" #Sem essa variavel: erro de non-define (nada consertou)
_MENU = "" # O menu tem cache... se alterar dinamicamente ou por qualquer razão, não vai... aconteceu na i18n

##########  - Trechos HTML

HTML_IMG = ''' <img src="%(img)s" class="menu" alt="%(titulo)s" title="%(titulo)s"/> '''

HTML_ITEM = """
    <li>
          <a href="%(url)s" style="width:%(width)spx;max-width:%(width)spx;">
              %(img)s
              <span>&nbsp;%(titulo)s&nbsp;</span>
          </a>
    </li>
"""

HTML_SUBMENU = """
    <a href="#" style='max-width:%(width)spx;'>
        %(img)s
        &nbsp;%(titulo)s&nbsp;
        <img  src="%(down_img)s" class="menu" alt="%(titulo)s" title="%(titulo)s"/>
    </a>
"""

##########  - Funções Auxiliares

get_image = lambda img: settings.STATIC_URL + img
get_image_or_not = lambda item : HTML_IMG%{"img"    : get_image(item["img"]),
                                           "titulo" : item["titulo"],
                                           } if item.has_key("img") else ""

## - Função de permissão

def _tem_permissao(perm_need_list):
    ## a implementar
    return True


########## - Funções de contrução de itens

def _make_menu_item(item, width):
    return HTML_ITEM%{
        "width" : width,
        "img"   : get_image_or_not(item),
        "titulo": item["titulo"],
        "url"   : reverse(item["url-name"]) if item.has_key("url-name") else item["url"] if item.has_key("url") else "#",
    }

def _make_submenu(item, width, submenu=False):
    return HTML_SUBMENU%{
        "width"    : width,
        "down_img" : get_image(_MENU["down_img"]),
        "img"      : get_image_or_not(item),
        "titulo"   : item["titulo"],
    }

########## - Função principal

def make_menu(user):
    global menu
    menu = ""
    global _MENU
    _MENU = MENU()
    return _make_menu_body(_MENU["itens"])

##########  - Função de construção de menu 
def _make_menu_body(menu_atual, width="auto"):
        global menu
        for item in menu_atual:
            
            # Verifica permissões, caso seja necessário
            if item.has_key("perm_need"):
                if item["perm_need"] and not _tem_permissao(item["perm_need"]):
                    continue # caso não tenha permissão, o item é ignorado
                
            # Verifica se é um submenu ou item de menu e renderiza
            if item.has_key("itens"):
                menu += "<li style='width:%(width)spx;'> %(sub_menu)s <ul  id='%(id-html)smenu'>"%{
                            'width'    : width,
                            'sub_menu' : _make_submenu(item,width),
                            'id-html'  : item["id-html"]}
                _make_menu_body(item["itens"],item["itens-width"])
                menu += "</ul></li>"
            else:
                menu += _make_menu_item(item, width)
                
        # Retorna os itens do menu/submenu e o próprio
        return menu

