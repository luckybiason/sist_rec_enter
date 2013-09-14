#-*- coding: utf-8 -*-
import pdb
from adm_rec.utils.decorators    import ajax_json_view
from adm_rec.utils.model_utils   import get_ids_str
from django.shortcuts            import redirect,render
from methods                     import *
from django.contrib              import messages
from televisores.models          import Televisor
from clientes.models             import Cliente
from televisores.methods_filtros import filtrar_precos, choices_tipos_tela_from
from models                      import USOS_CHOICES

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
    televisores_ids =  ";".join( [ str(tv.id) for tv in classificados] )
    
    ## Informações para o próximo passo
    aparelhos = APARELHOS_CHOICES
    
    ## Coleta de informações
    if request.session.get("id_cliente", ""):
        cliente      = Cliente.objects.get(pk=request.session.get("id_cliente"))
        cliente.usos = usos
        cliente.save()
    
    return render(request, "filtragem/passo2.html", locals())

def passo02(request):
    '''
     Passo 02: Quantidade de aparelhos. 
    '''
    ## Captura dos televisores 
    tvs_id = request.POST.get("tvs","")
    
    ## Captura dos aparelhos
    aparelhos = request.POST.getlist("aparelhos","")
    if not aparelhos:
        messages.error(request, "Informe pelo menos um aparelho.")
        
    ## Classificação
    televisores = Televisor.objects.filter(pk__in=tvs_id)
    televisores_ids = get_ids_str(classificacao_aparelhos(televisores, usos.split(',')) )
    
    ## Informações para o próximo passo
    preco_min, preco_max = get_max_min_preco_from_televisores(televisores)
    
    ## Coleta de informações
    if request.session.get("id_cliente", ""):
        cliente = Cliente.objects.get(pk=request.session.get("id_cliente"))
        cliente.aparelhos = aparelhos
        cliente.save()
        
    return render(request, "filtragem/passo03.html", locals())














def passo03(request):
    '''
     Passo 03: Faixa de preço. 
    '''
    ## Captura dos televisores 
    tvs_id = request.POST.get("tvs","")
    
    ## Captura dos precos
    preco_min = request.POST.get("preco_de","")
    preco_max = request.POST.get("preco_para","")
    if preco_min or preco_max: # Não obrigatório
        ## Classificação
        televisores     = Televisor.objects.filter(pk__in=tvs_id)
        televisores_ids = get_ids_str( filtrar_precos(preco_de, preco_para, televisores) )
    
    ## Construir choices para o passo 4
    tipos_telas = choices_tipos_tela_from(televisores, pelo_menos_um=True)
    
    return render(request, "filtragem/passo04.html", locals())

def passo05(request):
    '''
     Passo 05: Tamanho da tela. 
    '''
    ## Captura dos televisores 
    tvs_id = request.POST.get("tvs","")
    
    ## Captura dos tipos
    tipos = request.POST.get("tipos","")
    if preco_min or preco_max: # Não obrigatório
        ## Classificação
        televisores     = Televisor.objects.filter(pk__in=tvs_id)
        televisores_ids = get_ids_str( filtrar_tipos_tela(tipos.split(","), televisores) )
    
    return render(request, "filtragem/passo06.html", locals())

def passo06(request):
    '''
     Passo 01: Distância adequada. 
    '''
    ## Captura da distância
    distancia = request.POST.get("distancia","")
    if not distancia:
        messages.error(request, "Informa a distância entre o televisor e seu assento.")
        return redirect('portal.home')
    
    ## Classificação
    classificados   = classificacao_distancia(Televisor.objects.all(), float(distancia))
    televisores_ids =  ";".join([ str(item.id)+","+item.adequacao for item in classificados ])
    
    ## Informações para o passo 2
    
    return render(request, "filtragem/passo2.html", locals())