#-*- coding: utf-8 -*-
from adm_rec.utils.sql  import *
from filtragem.methods  import *
from televisores.models import Televisor

### - Recomendação (Motor) - ###

## 1) Filtragem

def filtrar_produtos(cliente):
    
    JOINS  = []
    WHERES = []
    
    # Filtragem de preços
    if cliente.preco_max or cliente.preco_min:
        JOINS.append('''
            INNER JOIN televisores_televisorloja as loja
                ON loja.televisor_id=televisores.id
        ''')
        WHERES.append(" ( loja.preco>=%s OR %s>=loja.preco )" % (cliente.preco_min, cliente.preco_max) )
        
    # Filtragem de tamanho de telas
    if cliente.tam_telas not in ("", "-", None):
        WHERES.append(" televisores.polegadas in ( %s ) " % cliente.tam_telas )
        
    # Filtragem de tipo de telas
    if cliente.tip_telas not in ("", "-", None):
        WHERES.append( " tipo_tela.descricao in (%s) " % \
                       ",".join( 
                                map( lambda tip: "'%s'" % tip, 
                                     cliente.tam_telas.split(",") 
                                ) 
                            ) 
                      )
    
    SQL = '''
        SELECT 
            distinct televisores.id as id_t
        FROM televisores
            %(JOINS)s
        WHERE 
            %(WHERES)s
        ORDER BY televisores.id
    ''' % {
           'JOINS' : "".join(JOINS)       if JOINS  else "",
           'WHERES': " AND ".join(WHERES) if WHERES else "(true)",
    }
    
    # Busca
    ids = sql_to_dict(SQL); print SQL
    televisores = Televisor.objects.filter(pk__in=map(lambda obj: obj["id_t"], ids));print "busca: ", televisores
        
    # Restante das classificações
    if cliente.usos not in ("", "-", None):
        tels = classificacao_uso(televisores, cliente.usos.split(",")) ;print "classificacao_uso: ", tels
        if tels: televisores = tels
    
    if cliente.aparelhos not in ("", "-", None):
        tels = classificacao_aparelhos(televisores, cliente.aparelhos.split(",")) ;print "classificacao_aparelhos: ", tels
        if tels: televisores = tels
        
    if cliente.aparelhos not in ("", "-", None):
        tels = classificacao_distancia(televisores, cliente.distancia);print "classificacao_distancia: ", tels
        if tels: televisores = tels
     
    return televisores   

## 2) Avaliação - remove produtos já vistos, comentados ou mal avaliados

def classificar_produtos(cliente, televisores):
    
    def remover_visitados(cliente, televisores):
        return filter(lambda tv: not tv.ja_visitado(cliente), televisores)
    
    def remover_nota_baixa(televisores):
        return filter(lambda tv: tv.get_nota_media>1, televisores)

    def remover_comentados(cliente, televisores):
        return filter(lambda tv: not tv.ja_comentado(cliente), televisores)
    
    tvs = remover_visitados(cliente, televisores) ;print "remover_visitados: ", tvs
    if tvs: televisores = tvs
    
    tvs = remover_nota_baixa(televisores) ;print "remover_nota_baixa: ", tvs
    if tvs: televisores = tvs
    
    tvs = remover_comentados(cliente, televisores) ;print "remover_comentados: ", tvs
    if tvs: televisores = tvs
    
    print "finais:", televisores
    return televisores


## Núcleo do fluxo da recomendação

def recomendar(cliente):
    ''' 
       Fluxo básico da recomandação:
        Entrada(cliente) --> filtragem --> avaliação --> Saida(itens)
        se filtragem nã0 retornar nada, retorna os 10 mais atuais
        se avaliação não retornar nada, retorna a filtragem
    '''
    if not cliente.has_perfil:
        return None
    
    televisores_filtrados = filtrar_produtos(cliente)
    
    if not televisores_filtrados:
        return Televisor.objects.order_by("-data_cadastro")[0:10]
    
    televisores_classificados = classificar_produtos(cliente, televisores_filtrados)
    
    if not televisores_classificados:
        return televisores_filtrados
    
    return televisores_classificados

