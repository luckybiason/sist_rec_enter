#-*- coding: utf-8 -*-

"""
    Colocar neste módulo as expressões regulares reutilizadas no sistema. 
"""

########## FUNÇÕES AUXILIARES ##########

def re_inicia(regex):
    " Retorna a regex recebida com um circunflexo (^) no início. "
    return '^%s' % regex

def re_termina(regex):
    " Retorna a regex recebida com um cifrão ($) no final. "
    return '%s$' % regex

def re_exata(regex):
    " Retorna a regex recebida com um circunflexo (^) no início e um cifrão ($) no final. "
    return re_termina(re_inicia(regex))


########## EXPRESSÕES REGULARES ##########

CPF = r'\d{3}\.?\d{3}\.?\d{3}-?\d{2}'

DATA = r'(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/\d{4}'

EMAIL = r'^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$'

ENDERECO_IP = r'^(([01]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.){3}([01]?[0-9]{1,2}|2[0-4][0-9]|25[0-5]){1}$'

MULTIPLOS_ESPACOS = r'\s{2,}'

# Número completo de celular, com código do país e código de área (DDD)
# 55DDNNNNNNNN: 55 -> Cod. país; DD -> Cod. área (DDD); NNNNNNNN -> Número do celular (8 ou 9 dígitos)
CELULAR_COMPLETO = r'^\d{2}\d{2}\d{8,9}$'

