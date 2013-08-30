#-*- coding: utf-8 -*-
from django.shortcuts   import render
from methods_busca      import buscar_produtos
from televisores.models import Televisor, Marca, TelevisorLoja
from portal.models      import Comentario
from adm_rec.utils.paginators import makePaginator
from portal.methods_filtros   import selecionar, filtrar, prepare, get_filtros

#def buscar(request):
#    ''' Função de busca de produtos no site '''
#    produtos = buscar_produtos(request)
#    return render(request, 'busca/listagem_produtos.html', locals())

def buscar(request):
    ''' Função de busca de produtos no site '''
    
    ## Seleção e filtragem
    produtos = selecionar(request)
    produtos = filtrar(request, produtos)
    
    ## Cache
    id_produtos = ",".join( [ str(obj.id) for obj in produtos] )
    
    ## Paginação e Informações adicionais
    num_pag, page, paginator = makePaginator(request,produtos,group=8)
    page.object_list = prepare(request, page.object_list)
    
    ## Informações para filtragem
    marcas, precos, telas, informacoes = get_filtros(request, produtos)
    
    return render(request, 'portal/listagem_produtos.html', locals())