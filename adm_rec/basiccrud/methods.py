#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import *

##- Função para criação/ definição das urls
def catch_urls(model):
        appname     = model.get_config()["app"]
        url_context = {
                       'cadastro'   : appname+".cadastro",
                       'excluir'    : appname+".excluir",
                       'listagem'   : appname+".listagem",
                       'detail_ajax': appname+".getdetail",
        }
        return url_context
