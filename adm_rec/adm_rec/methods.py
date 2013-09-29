#-*- coding: utf-8 -*-
from utils.sql import *

def numero_por_mes_atual(tabela):
    sql_datas = '''
        SELECT count(id), data_cadastro 
        FROM %(tabela)s
        WHERE EXTRACT( month from data_cadastro) = EXTRACT(month from current_date)
        GROUP by data_cadastro
    ''' % { 
        'tabela' : tabela, 
    }
    datas = sql_to_dict(sql_datas)
    return [ {'num':int(res['count']) , 'data':int(res['data_cadastro'].strftime("%d"))} for res in datas]
    
def numero_por_ano(tabela):
    sql_datas = '''
        select 
           count(id),
           EXTRACT( year from data_cadastro) as ano, 
           EXTRACT( month from data_cadastro)  as mes
        from %(tabela)s
        group by EXTRACT( year from data_cadastro), EXTRACT( month from data_cadastro)
    ''' % { 
        'tabela' : tabela, 
    }
    datas = sql_to_dict(sql_datas)
    return [ { 'num':int(res['count']) , 'mes':res['mes'], 'ano':res['ano'] } for res in datas]
    
def numero_por_ano_atual(tabela):
    sql_datas = '''
        select 
           count(id),
           EXTRACT( year from data_cadastro) as ano, 
           EXTRACT( month from data_cadastro)  as mes
        from %(tabela)s
        where EXTRACT( year from data_cadastro) = EXTRACT(year from current_date)
        group by EXTRACT( year from data_cadastro), EXTRACT( month from data_cadastro)
    ''' % { 
        'tabela' : tabela, 
    }
    datas = sql_to_dict(sql_datas)
    return [ { 'num':int(res['count']) , 'mes':res['mes'] } for res in datas]
    