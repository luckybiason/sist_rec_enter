#-*- coding: utf-8 -*-
from django.db.models import Max, Min
from televisores.models import Televisor, TelevisorLoja, TipoTela, Marca

### -  Filtragem Menu de lojas - ###
def filtrar_por_lojas(loja, televisores=None):
    if not televisores:
        televisores =  TelevisorLoja
    televisores = televisores.objects.filter(loja__id__in=loja)
    return televisores

def quantidade_por_lojas(loja, televisores=None):
    return filtrar_por_lojas(loja, televisores).count()

def choices_with_qntd_lojas():
    return [ (loja.id, loja.nome,quantidade_por_lojas(loja) )  for marca in Marca.objects.all() ]

def choices_marcas_from(televisores):
    return tuple(set([ (tel.marca.id, tel.marca.descricao)  for tel in televisores ]))

def choices_with_qntd_marcas_from(televisores):
    return list(set([ (tel.marca.id, tel.marca.descricao,quantidade_por_marca(tel.marca) ) for tel in televisores ]))



### -  Filtragem Menu de marcas - ###
def filtrar_por_marcas(marca, televisores=None):
    if not televisores:
        televisores =  Televisor
    televisores = televisores.objects.filter(marca__id=marca)
    return televisores

def quantidade_por_marcas(televisores=None):
    return filtrar_por_marcas(televisores).count()

def choices_marcas():
    return tuple([ (marca.id, marca.descricao)  for marca in Marca.objects.all() ])

def choices_with_qntd_marcas():
    return [ (marca.id, marca.descricao,quantidade_por_marcas(tipo) )  for marca in Marca.objects.all() ]

def choices_marcas_from(televisores):
    return tuple(set([ (tel.marca.id, tel.marca.descricao)  for tel in televisores ]))

def choices_with_qntd_marcas_from(televisores):
    return list(set([ (tel.marca.id, tel.marca.descricao,quantidade_por_marca(tel.marca) ) for tel in televisores ]))


### -  Filtragem Menu de preços - ###
def filtrar_precos(de=0, ate=0, televisores=None):
    if not de and not ate:
        televisores = TelevisorLoja.objects.all()
    televisores = TelevisorLoja.objects.filter(preco__gte=de,preco__lte=ate)
    return televisores
    
TIPO_PRECO = {
    '1' : {""},
    '2' : {'de' : 500},
    '3' : {'ate': 1000},
    '4' : {'ate': 2000},
    '5' : {'de' : 2000},
}

def filtrar_por_preco(preco, televisores=None):
    televisores = filtrar_precos(**TIPO_PRECO[preco])
    return televisores

def quantidade_por_preco(preco):
    return filtrar_por_preco(preco, televisores).count()

def get_max_min_preco_from_televisor(televisor):
    lojas = TelevisorLoja.objects.filter(televisor=televisor)
    max = lojas.aggregate(Max('preco'))
    min = lojas.aggregate(Min('preco'))
    return min, max

def get_max_min_preco_from_televisores(televisores):
    max_return, min_return = 0
    for televisor in televisores:
        max, min = get_max_min_preco_from_televisor(televisor)
        if max_return<max: max_return=max
        if min_return>min: min_return=min
    return min_return, max_return

### -  Filtragens de tipos de telas - ###
def filtrar_tipos_tela(tipos, televisores=None):    
    if not televisores:
        televisores =  Televisor
    televisores = televisores.objects.filter(tipo_de_tela__in=tipos)
    return televisores

def quantidade_por_tipos_tela(tipos):
    return filtrar_tipos_tela(tipos, televisores).count()

def choices_tipos_tela():
    return tuple([ (tipo.id, tipo.descricao)  for tipo in TipoTela.objects.all() ])

def choices_with_qntd_tipos_tela():
    return [ (tipo.id, tipo.descricao,quantidade_por_tipos_tela(tipo) )  for tipo in TipoTela.objects.all() ]

def choices_tipos_tela_from(televisores):
    return tuple(set([ (tel.tipo_de_tela.id, tel.tipo_de_tela.descricao)  for tel in televisores ]))

def choices_with_qntd_tipos_tela_from(televisores):
    return list(set([ (tel.tipo_de_tela.id, tel.tipo_de_tela.descricao,quantidade_por_tipos_tela(tel.tipo_de_tela) ) for tel in televisores ]))

