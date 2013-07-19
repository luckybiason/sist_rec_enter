# -*- coding: utf-8 -*-
from utils.decorators     import ajax_json_view
from app_endereco.methods import *

@ajax_json_view
def carrega_cidades_do_estado(request):
    sigla_uf = request.GET.get('sigla_uf').upper()
    cidades  = busca_cidades(uf)
    return [ {'cod_cidade': cidade[0], 
              'nome'      : cidade[1]} for cidade in cidades ]

@ajax_json_view
def get_nome_cidade(request, cod_cidade):
    try:
        return busca_cidade(cod_cidade)
    except:
        return ''
