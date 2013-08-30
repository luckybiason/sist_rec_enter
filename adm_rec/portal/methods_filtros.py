#-*- coding: utf-8 -*-
from methods_busca      import buscar_produtos
from televisores.models import Televisor, Marca, TelevisorLoja, TipoTela
from portal.models      import Comentario
from adm_rec.utils.paginators    import makePaginator
from televisores.methods_filtros import choices_with_qntd_marcas_from, choices_with_qntd_preco_from, \
                                        choices_with_qntd_tipos_tela_from, choices_with_qntd_infos_from,\
                                        filtrar_por_preco, filtrar_por_marcas, filtrar_tipos_tela, filtrar_infos

def selecionar(request):
    ''' Função de busca de produtos no site '''
    
    ## Seleção de Produtos
    if (request.GET.get("pesq_busca","")): # Via busca por palavra chave
        produtos = buscar_produtos(request)
    elif (request.GET.get("ids_produtos","")): # Via página de vitrine / seleção
        produtos = Televisor.objects.filter(pk__in=request.GET.get("ids_produtos","").split(','))
    else:
        produtos = Televisor.objects.all() # Via 'Todos os produtos'
        
    return produtos
   
def filtrar(request, produtos):
    ''' Função de filtragem de produtos para a vitrine '''
    
    # - Filtragens
    if request.GET.get("marcas_ids",""):
        ids_marcas = filter(lambda id: id.isdigit(), request.GET.get("marcas_ids",""))
        marcas     = Marca.objects.filter(pk__in=ids_marcas)
        produtos   = filtrar_por_marcas(marcas, televisores=produtos)
    
    if request.GET.get("preco_id",""):
        produtos = filtrar_por_preco(request.GET.get("preco_id",""), televisores=produtos)
    
    if request.GET.get("telas_ids",""):
        ids_telas = filter(lambda id: id.isdigit(), request.GET.get("telas_ids",""))
        telas     = TipoTela.objects.filter(pk__in=ids_telas)
        produtos  = filtrar_tipos_tela(telas, televisores=produtos)
            
    if request.GET.get("infos_ids",""):
        ids_infos = filter(lambda id: id.isdigit(), request.GET.get("infos_ids",""))
        produtos  = filtrar_infos(ids_infos, televisores=produtos)
        
    return produtos

def prepare(request, produtos):
    ''' Função que complementa informações aos produtos para a vitrine '''
        
    ## Informações adicionais para os produtos
    for produto in produtos:
        lojas = TelevisorLoja.objects.filter(televisor=produto).values_list('preco', flat=True)
        produto.maior_preco = max(lojas)
        produto.menor_preco = min(lojas)
        coments = Comentario.objects.filter(televisor=produto).values_list('nota', flat=True)
        if coments:
            produto.nota_media  = reduce(lambda x,y: x+y, coments)/len(coments)
    
    return produtos

def get_filtros(request, produtos):
    ''' Função que cria as opções de filtros para a vitrine '''
        
    # - Informações para filtragem
    # Marcas
    marcas = choices_with_qntd_marcas_from(produtos, pelo_menos_um=True)
    # Preços
    precos = choices_with_qntd_preco_from(produtos, pelo_menos_um=True) 
    # Tamanho da tela
    telas  = choices_with_qntd_tipos_tela_from(produtos, pelo_menos_um=True) 
    # Informações/Caracteristicas
    informacoes = choices_with_qntd_infos_from(produtos, pelo_menos_um=True)
    
    return marcas, precos, telas, informacoes

