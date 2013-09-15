#-*- coding: utf-8 -*-
import pdb
from adm_rec.utils.decorators    import ajax_json_view
from adm_rec.utils.model_utils   import get_ids_str
from django.shortcuts            import redirect,render
from methods                     import *
from django.contrib              import messages
from televisores.models          import Televisor
from clientes.models             import Cliente
from televisores.methods_filtros import *
from televisores.models          import *
from models                      import USOS_CHOICES
from adm_rec.utils.paginators    import makePaginator
from portal.methods_filtros      import selecionar, filtrar, prepare, get_filtros

def passo01(request):
    '''
     Passo 01: Uso. 
    '''
    ## Captura dos usos
    usos = request.POST.getlist("usos","")
    if not usos:
        messages.error(request, "Informe pelo menos um uso.")
        return redirect('portal.home')
        
    ## Classificação
    televisores     = Televisor.objects.all()
    classificados   = classificacao_uso(televisores, usos )
    televisores_ids = ";".join( [ str(tv.id) for tv in classificados] )
    
    ## Informações para o próximo passo
    aparelhos = APARELHOS_CHOICES
    
    ## Coleta de informações
    if request.session.get("id_cliente", ""):
        cliente      = Cliente.objects.get(pk=request.session.get("id_cliente"))
        cliente.usos = ",".join(usos)
        cliente.save()
    
    return render(request, "filtragem/passo2.html", locals())

def passo02(request):
    '''
     Passo 02: Quantidade de aparelhos. 
    '''
    ## Captura dos televisores 
    tvs_id = request.POST.get("tvs_ids","")
    
    ## Captura dos aparelhos
    aparelhos = request.POST.getlist("aparelhos","")
    if not aparelhos:
        messages.error(request, "Informe pelo menos um aparelho.")
        aparelhos = APARELHOS_CHOICES
        televisores_ids = tvs_id
        return redirect('filtragem.passo01')
        
    ## Classificação
    televisores     = Televisor.objects.filter(pk__in=tvs_id.split(";"))
    classificados   = classificacao_aparelhos(televisores, aparelhos )
    televisores_ids = ";".join( [ str(tv.id) for tv in classificados] )
    
    ## Informações para o próximo passo
    #preco_min, preco_max = get_max_min_preco_from_televisores(televisores)
    
    ## Coleta de informações
    if request.session.get("id_cliente", ""):
        cliente = Cliente.objects.get(pk=request.session.get("id_cliente"))
        cliente.aparelhos = ",".join(aparelhos)
        cliente.save()
        
    return render(request, "filtragem/passo3.html", locals())


def passo03(request):
    '''
     Passo 03: Faixa de preço. 
    '''
    ## Captura dos televisores 
    televisores_ids = request.POST.get("tvs","")
    classificados   = Televisor.objects.filter(pk__in=televisores_ids)
    
    ## Captura dos precos
    preco_min, preco_max = '', ''
    if request.POST.get("preco_de","") and request.POST.get("preco_para",""):
        preco_min   = float(request.POST.get("preco_de","0").replace(",","."))
        preco_max   = float(request.POST.get("preco_para","0").replace(",","."))
        
        if preco_min or preco_max: # Não obrigatório
            ## Classificação
            classificados   = filtrar_precos(preco_min, preco_max, classificados)
            televisores_ids = get_ids_str(classificados)
    
    ## Coleta de informações
    if request.session.get("id_cliente", ""):
        cliente = Cliente.objects.get(pk=request.session.get("id_cliente"))
        cliente.preco_min = preco_min or 0.0
        cliente.preco_max = preco_max or 0.0
        cliente.save()
    
    ## Construir choices para o passo 4
    tamanhos = choices_tam_tela_from(classificados)
    
    return render(request, "filtragem/passo4.html", locals())

def passo04(request):
    '''
     Passo 04: Tamanho da tela. 
    '''
    ## Captura dos televisores 
    televisores_ids = request.POST.get("tvs","")
    classificados   = Televisor.objects.filter(pk__in=televisores_ids)
    
    ## Captura dos tamanhos
    tam_telas = [ tam.replace(",",".") for tam  in request.POST.getlist("tamanhos","")]
    
    # Classificação
    if tam_telas:
        classificados   = filtrar_tam_tela(tam_telas, classificados)
        televisores_ids = get_ids_str( classificados )
    
    ## Coleta de informações
    if request.session.get("id_cliente", ""):
        cliente = Cliente.objects.get(pk=request.session.get("id_cliente"))
        cliente.tam_telas = ",".join(tam_telas) 
        cliente.save()
    
    ## Construir choices para o passo 5
    tipos = TipoTela.objects.filter(pk__in= [ ch[0] for ch in choices_tipos_tela_from(classificados)] )
    
    return render(request, "filtragem/passo5.html", locals())


def passo05(request):
    '''
     Passo 05: Tipo da tela. 
    '''
    ## Captura dos televisores 
    tvs_id = request.POST.get("tvs","")
    
    ## Captura dos tamanhos
    tip_telas = ""
    
    ## Coleta de informações
    if request.session.get("id_cliente", ""):
        cliente = Cliente.objects.get(pk=request.session.get("id_cliente"))
        cliente.tip_telas = tip_telas
        cliente.save()
    
    return render(request, "filtragem/passo6.html", locals())


def passo06(request):
    '''
     Passo 01: Distância adequada. 
    '''
    ## Captura da distância
    distancia = request.POST.get("distancia","")
    if not distancia:
        messages.error(request, "Informa a distância entre o televisor e seu assento.")
        return redirect('filtragem.passo05')
    
    ## Classificação
    classificados   = classificacao_distancia(Televisor.objects.all(), float(distancia))
    televisores_ids =  ";".join([ str(item.id)+","+item.adequacao for item in classificados ])
    
    
    ## Coleta de informações
    if request.session.get("id_cliente", ""):
        cliente = Cliente.objects.get(pk=request.session.get("id_cliente"))
        cliente.distancia = distancia
        cliente.save()
    
    ## Informações para a tela de listagem
    
    ## Cache
    id_produtos = ",".join( [ str(obj.id) for obj in classificados] )
    
    ## Paginação e Informações adicionais
    num_pag, page, paginator = makePaginator(request,classificados,group=8)
    page.object_list = prepare(request, page.object_list)
    
    ## Informações para filtragem
    marcas, precos, telas, informacoes = get_filtros(request, classificados)
    
    
    return render(request, "portal/listagem_produtos.html", locals())