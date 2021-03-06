#-*- coding: utf-8 -*-
from django.conf import settings
from django.db import connections, transaction


def sql_to_dict(select_sql, param=None, database_alias='default'):
    """
        Executa a query 'select_sql' no banco, passando o 'param' como parâmetro para o cursor,
        e retorna o resultado da query, com cada linha convertida em um dicionário.
        O parâmetro 'database_alias' é o alias do banco de dados contra o qual será executado o select.
        Os aliases possíveis são as chaves do dicionário 'DATABASES', que fica nas settings.
    """
    assert settings.DATABASES.has_key(database_alias)

    cursor = connections[database_alias].cursor()
    cursor.execute(select_sql, param)
    nomes_campos = [nome[0] for nome in cursor.description]
    retorno = []
    for linha in cursor.fetchall():
        lista_linha = []
        for campo in zip(nomes_campos, linha):
            lista_linha.append(campo)
        retorno.append(dict(lista_linha))
    return retorno


def consulta_valor_escalar_no_banco(select_sql, database_alias='default'):
    """
        Executa a query 'select_sql' no banco e retorna o valor da primeira coluna da primeira linha retornada pela query.
        O parâmetro 'database_alias' é o alias do banco de dados contra o qual será executado o select.
        Os aliases possíveis são as chaves do dicionário 'DATABASES', que fica nas settings.
    """
    assert settings.DATABASES.has_key(database_alias)

    cursor = connections[database_alias].cursor()
    cursor.execute(select_sql)
    retorno = cursor.fetchone() 
    return retorno[0] if retorno else None


def sql_escape(valor):
    return valor.replace(r'%','').replace("'","''")
    