#-*- coding: utf-8 -*-
from django.shortcuts  import render
from methods_busca   import buscar_produtos

def buscar(request):
    ''' Função de busca de produtos no site '''
    produtos = buscar_produtos(request)
    return render(request, 'busca/listagem_produtos.html', locals())