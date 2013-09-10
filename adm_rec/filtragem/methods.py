#-*- coding: utf-8 -*-
from models import *
from televisores.methods_filtros import filtrar_precos, filtrar_tipos_tela, get_max_min_preco_from_televisores
from televisores.models          import Entrada

#filtrar_precos(de=0, ate=0, televisores=None)
#get_max_min_preco_from_televisores(televisores)
#filtrar_tipos_tela(tipos, televisores=None)

##===============================##
## - Funções de classificação  - ##
##===============================##
    
def classifica_por_distancia(televisor,distancia):
    '''
       Classifica o televisor de acordo com a distância.
       Recebe dois parâmetros:
       - televisor : o televisor a ser classificado
       - distancia : a distancia informada pelo cliente
       Retorna False caso a porcentagem da diatncia seja inferior a 20%
       Retorna o televisor com uma marcação.
       Caso a porcentagem seja entre 90% e 100%, a marca será “Adequada”.
       Caso a porcentagem seja entre 50% e 89%,  a marca será “Atenção”
       Caso a porcentagem seja entre 20% e 49%,  a marca será “Inadequada”.      
    '''
    # Calculo da porcentagem de adequação a distância
    tamanho_ideal = televisor.polegadas*4.14
    porcentagem   = (distancia*100)/tamanho_ideal
    
    # Classificação
    if porcentagem<20:
        return False
    
    if porcentagem<50:
        televisor.adequacao = "Inadequado"
    elif porcentagem<90:
        televisor.adequacao = "Atenção"
    else:   
        televisor.adequacao = "Adequado"
    
    return televisor

def classifica_por_uso(televisor, usos):
    '''
       Classifica o televisor de acordo com os usos.
       Recebe dois parâmetros:
       - televisor : o televisor a ser classificado
       - usos : uma lista contendo os usos selecionados
       Retorna True ou False
    '''
    if not televisor.resolucao:
        return False
    
    for uso in usos:
        if USOS_PESOS[televisor.resolucao]>=USOS_PESOS[uso]:
            return True

def classifica_por_aparelhos(televisor, entradas):
    return True

##===============================##
## - Motores de classificação  - ##
##===============================##

def classificacao_distancia(televisores, distancia):
    classificados = []
    for televisor in televisores:
        retorno = classifica_por_distancia(televisor,distancia)
        if retorno:
            classificados.append(retorno)
    return classificados

def classificacao_uso(televisores, usos):
    classificados = []
    for televisor in televisores:
        retorno = classifica_por_uso(televisor,usos)
        if retorno:
            classificados.append(retorno)
    return classificados

def classificacao_aparelhos(televisores, aparelhos):
    
    # Montar lista de conexoes
    entradas_desc = list(set([ info[0] for (key,info) APARELHOS_INFO.items() if key in aparelhos ]))
    entradas = []
    for entrada in entradas_desc:
        entradas += map( lambda entrada: entrada.entrada.id, Entrada.objects.filter(descricao__icontains=entrada) )
    
    # Filtragem
    classificados =[]
    for televisor in televisores:
        classificado.append( classifica_por_aparelhos(televisor, entradas) )
    
    
    
    
    