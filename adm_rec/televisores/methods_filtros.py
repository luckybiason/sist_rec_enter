#-*- coding: utf-8 -*-
from django.db.models   import Q, Max, Min
from televisores.models import Televisor, TelevisorLoja, TipoTela, Marca

#==================================================#
# --- Utilidades para filtragem de televisores --- #
#==================================================#

############################################################
########## -  Filtragem Menu de Marcas (INICIO) - ##########

def filtrar_por_marcas(marcas, televisores=None):
    ''' Filtragem por marcas '''
    ids_marcas = [ marca.id for marca in marcas]
    
    if not televisores:
        return Televisor.objects.filter(marca__id__in=ids_marcas)
    
    return filter(lambda tv: tv.marca.id in ids_marcas , televisores)

def quantidade_por_marcas(marca, televisores=None):
    ''' Retorna a quantidade de televisores na coleção ou banco de uma determinada marca '''
    return len(filtrar_por_marcas(marca, televisores))

def choices_marcas(pelo_menos_um=False):
    ''' 
        Retorna um choice para marcas cadastradas no banco de dados.
        Ao ser passado o parâmetro pelo_menos_um (opcional) como True, retorna apenas as marcas com 
        pelo menos um televisor cadastrado com elas.
    '''    
    if pelo_menos_um:
        return tuple([ (marca.id, marca.descricao) for marca in Marca.objects.all() if quantidade_por_marcas([marca])  ])
    
    return tuple([ (marca.id, marca.descricao) for marca in Marca.objects.all() ])

def choices_with_qntd_marcas():
    ''' 
        Retorna um choice com quantidade para marcas cadastradas no banco de dados.
    '''    
    return [ (marca.id, marca.descricao, quantidade_por_marcas([tipo]) )  for marca in Marca.objects.all() ]

def choices_marcas_from(televisores, pelo_menos_um=False):
    ''' 
        Retorna um choice para marcas cadastradas dos televisores passados.
        Ao ser passado o parâmetro pelo_menos_um (opcional) como True, retorna apenas as marcas com 
        pelo menos um televisor cadastrado com elas.
    '''    
    if pelo_menos_um:
        return tuple(set([ (tel.marca.id, tel.marca.descricao) for tel in televisores if quantidade_por_marcas([tel.marca], televisores) ]))
    
    return tuple(set([ (tel.marca.id, tel.marca.descricao)  for tel in televisores ]))

def choices_with_qntd_marcas_from(televisores, pelo_menos_um=True):
    ''' 
        Retorna um choice com quantidade para marcas cadastradas nos televisores.
        Ao ser passado o parâmetro pelo_menos_um (opcional) como True, retorna apenas as marcas com 
        pelo menos um televisor cadastrado com elas.
    '''    
    choices = list(set([ (tel.marca.id, 
                          tel.marca.descricao, 
                          quantidade_por_marcas([tel.marca],televisores) ) for tel in televisores ]))
    
    if pelo_menos_um:
        return filter(lambda marca: marca[2]!=0, choices)
    
    return choices

########### -  Filtragem Menu de marcas (FIM) - ###########
###########################################################

############################################################
########## -  Filtragem Menu de Preços (INICIO) - ##########

# Verifica se o televisor esta entre os precos 'de' e 'ate'
between_prices = lambda de, ate, tv: TelevisorLoja.objects.filter( Q(televisor__id=tv.id) & Q(preco__gte=de) & Q(preco__lte=ate)).exists()

def filtrar_precos(de=0, ate=0, televisores=None):
    ''' Filtragem por preços '''
    
    if not de and not ate:
        return televisores if televisores else Televisor.objects.all()
    
    if televisores:
        return [ tv for tv in televisores if between_prices(de, ate, tv) ]
    
    return [tl.televisor for tl in TelevisorLoja.objects.filter(preco__gte=de,preco__lte=ate) ]

TVS_PRECOS = [
    ('1', u"Todos",                     lambda televisores : (0,    0,    televisores)),
    ('2', u"até R$ 500,00",             lambda televisores : (0,    500,  televisores)),
    ('3', u"R$ 500,00 até R$ 1000,00",  lambda televisores : (501,  1000, televisores)),
    ('4', u"R$ 1000,00 até R$ 2000,00", lambda televisores : (1001, 2000, televisores)),
    ('5', u"Mais de R$ 2000,00",        lambda televisores : (2001, 99999999, televisores)),
]

TIPO_PRECO  = { inf[0]:inf[2] for inf in TVS_PRECOS }
LABEL_PRECO = { inf[0]:inf[1] for inf in TVS_PRECOS }

def filtrar_por_preco(preco, televisores=None):
    ''' Retorna televisores na coleção ou banco de uma determinada faixa de preço '''
    return filtrar_precos(*TIPO_PRECO[preco](televisores))

def quantidade_por_preco(preco, televisores=None):
    ''' Retorna a quantidade de televisores na coleção ou banco de uma determinada faixa de preço '''
    return len(filtrar_por_preco(preco, televisores))

def choices_with_qntd_preco_from(televisores, pelo_menos_um=False):
    ''' 
        Retorna um choice para marcas cadastradas dos televisores passados.
        Ao ser passado o parâmetro pelo_menos_um (opcional) como True, retorna apenas o precos com 
        pelo menos um televisor cadastrado com eles.
    '''    
    choices =  [ (key, 
                  LABEL_PRECO[key], 
                  quantidade_por_preco(key, televisores) ) for (key, value) in TIPO_PRECO.items() ]
    
    if pelo_menos_um:
        return filter(lambda preco: preco[2]!=0, choices)
    
    return choices

def get_max_min_preco_from_televisor(televisor):
    ''' 
        Retorna o preço minimo e máximo de um televisor de acordo com suas lojas
    '''    
    lojas = TelevisorLoja.objects.filter(televisor=televisor)
    max   = lojas.aggregate(Max('preco'))
    min   = lojas.aggregate(Min('preco'))
    return min, max


def get_max_min_preco_from_televisores(televisores):
    ''' 
        Retorna o preço minimo e máximo de um conjunto de televisores de acordo com suas lojas
    '''    
    max_return, min_return = 0
    for televisor in televisores:
        max, min = get_max_min_preco_from_televisor(televisor)
        if max_return<max: max_return=max
        if min_return>min: min_return=min
    return min_return, max_return

########### -  Filtragem Menu de Preços (FIM) - ###########
###########################################################

###################################################################
########## -  Filtragem Menu de Tipos de Tela (INICIO) - ##########

def filtrar_tipos_tela(tipos, televisores=None):
    ''' Filtragem por tipos de tela ''' 
    ids_tipos = [ tipo.id for tipo in tipos]
    if not televisores:
        return Televisor.objects.filter(tipo_de_tela__id__in=ids_tipos)
    
    return filter(lambda tv: tv.tipo_de_tela.id in ids_tipos , televisores)

def quantidade_por_tipos_tela(tipos, televisores=None):
    ''' Retorna a quantidade de televisores na coleção ou banco de um determinado tipo de tela '''
    return len(filtrar_tipos_tela(tipos, televisores))

def choices_tipos_tela(pelo_menos_um=False):
    ''' 
        Retorna um choice para os tipos de tela cadastradas no banco de dados.
        Ao ser passado o parâmetro pelo_menos_um (opcional) como True, retorna apenas os tipos com 
        pelo menos um televisor cadastrado com eles.
    '''    
    if pelo_menos_um:
        return tuple([ (tipo.id, tipo.descricao) for tipo in TipoTela.objects.all() if quantidade_por_tipos_tela([tipo])  ])
    
    return tuple([ (tipo.id, tipo.descricao)  for tipo in TipoTela.objects.all() ])

def choices_with_qntd_tipos_tela(televisores):
    ''' 
        Retorna um choice com quantidade para os tipos de tela cadastrados no banco de dados.
    '''    
    return [ (tipo.id, tipo.descricao,quantidade_por_tipos_tela([tipo], televisores) )  for tipo in TipoTela.objects.all() ]

def choices_tipos_tela_from(televisores, pelo_menos_um=False):
    ''' 
        Retorna um choice para os tipos de tela cadastrados dos televisores passados.
        Ao ser passado o parâmetro pelo_menos_um (opcional) como True, retorna apenas os tipos de tela com 
        pelo menos um televisor cadastrado com elas.
    '''    
    if pelo_menos_um:
        return tuple(set([ (tel.tipo_de_tela.id, tel.tipo_de_tela.descricao) for tel in televisores \
                                                                             if quantidade_por_tipos_tela([tel.tipo_de_tela]) ]))
    
    return tuple(set([ (tel.tipo_de_tela.id, tel.tipo_de_tela.descricao)  for tel in televisores ]))

def choices_with_qntd_tipos_tela_from(televisores, pelo_menos_um=True):
    ''' 
        Retorna um choice com quantidade para marcas cadastradas nos televisores.
        Ao ser passado o parâmetro pelo_menos_um (opcional) como True, retorna apenas as marcas com 
        pelo menos um televisor cadastrado com elas.
    '''    
    choices = list(set([ (tel.tipo_de_tela.id, 
                          tel.tipo_de_tela.descricao,
                          quantidade_por_tipos_tela([tel.tipo_de_tela], televisores) ) for tel in televisores ]))
    
    if pelo_menos_um:
        return filter(lambda tela: tela[2]!=0, choices)
    
    return choices


###################################################################
########### -  Filtragem Menu de Informações (INICIO) - ###########

TVS_INFOS = [
    ('1', u"Full HD",           lambda tv: tv.is_full_hd),
    ('2', u"Smart TV",          lambda tv: tv.is_smart_tv),
    ('3', u"HDTV",              lambda tv: tv.is_hdtv),
    ('4', u"3D",                lambda tv: tv.is_3d),
    ('5', u"Conversor Digital", lambda tv: tv.has_conversor)
]

DICT_INFOS  = { inf[0]:inf[2] for inf in TVS_INFOS }
LABEL_INFOS = { inf[0]:inf[1] for inf in TVS_INFOS }

pass_tests = lambda tv, infos : any( [ True for info in infos if info(tv) ] )

def filtrar_infos(infos, televisores=None):
    ''' Filtragem por Informações '''
    if not infos: 
        return televisores or Televisor.objects.all()
    
    tests_info = [ DICT_INFOS[info] for info in infos ]
    
    if not televisores:
        return [ tv for tv in Televisor.objects.all() if pass_tests(tv, tests_info) ]
    
    return [ tv for tv in televisores if pass_tests(tv, tests_info) ]

def filtrar_por_info(infos, televisores=None):
    ''' Retorna televisores na coleção ou banco que tenha uma das flags infos '''
    return filtrar_infos(infos, televisores)

def quantidade_por_info(info, televisores):
    ''' Retorna a quantidade de televisores na coleção ou banco que tenha uma das flags infos '''
    return len(filtrar_por_info([info], televisores))

def choices_with_qntd_infos_from(televisores, pelo_menos_um=False):
    ''' 
        Retorna um choice para marcas cadastradas dos televisores passados.
        Ao ser passado o parâmetro pelo_menos_um (opcional) como True, retorna apenas o precos com 
        pelo menos um televisor cadastrado com eles.
    '''    
    choices = [ (key, 
                 LABEL_INFOS[key], 
                 quantidade_por_info(key, televisores) ) for (key, value) in DICT_INFOS.items() ]
    
    if pelo_menos_um:
        return filter(lambda info: info[2]!=0, choices)
    
    return choices



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

def choices_lojas_from(televisores):
    return tuple(set([ (tel.marca.id, tel.marca.descricao)  for tel in televisores ]))

def choices_with_qntd_lojas_from(televisores):
    return list(set([ (tel.marca.id, tel.marca.descricao,quantidade_por_lojas(tel.marca) ) for tel in televisores ]))

