#-*- coding: utf-8 -*-

import re
import RegExps
from random import choice
from string import ascii_letters, digits, whitespace


def apenas_digitos(valor, default=None):
    """
        Recebe uma string ('valor') e retorna uma cópia dela contendo
        apenas dígitos (removendo outros caracteres).
        Se o resultado for uma string vazia, o valor retornado
        será o que for passado para o parâmetro 'default'.
    """
    return ''.join([ c for c in str(valor) if c.isdigit() ]) or default


def ltrim(texto):
    """
        Retorna o texto com os espaços à esquerda eliminados.
    """
    retorno = ''
    achou_caractere = False
    for c in texto:
        if not achou_caractere:
            if c in whitespace:
                continue
            else:
                retorno += c
                achou_caractere = True
        else:
            retorno += c
    return retorno


def rtrim(texto):
    """
        Retorna o texto com os espaços à direita eliminados.
    """
    retorno_inv = ''
    achou_caractere = False
    for c in reversed(texto):
        if not achou_caractere:
            if c in whitespace:
                continue
            else:
                retorno_inv += c
                achou_caractere = True
        else:
            retorno_inv += c
    retorno = ''.join([c for c in retorno_inv])
    retorno = ''.join([c for c in reversed(retorno)])
    return retorno


def trim(texto):
    """
        Retorna o texto com os espaços à esquerda e à esquerda eliminados.
    """
    return ltrim(rtrim(texto))


def trim_in_and_out(valor):
    """
        Remove espaços antes e depois do texto.
        Também substitui múltiplos espaços entre as palavras por espaços únicos.
    """
    retorno = re.sub(RegExps.MULTIPLOS_ESPACOS, ' ', valor)
    retorno = trim(retorno)
    return retorno


def del_acento(s):
    """
        Recebe uma string e a retorna com os acentos removidos
    """
    
    dict_conversao = {
        'a': ['á', 'à', 'â', 'ä', 'ã', 'å'],
        'ae': ['æ'],
        'c': ['ç'],
        'd': ['Þ'],
        'e': ['é', 'è', 'ê', 'ë'],
        'i': ['í', 'ì', 'î', 'ï'],
        'n': ['n'],
        'o': ['ó', 'ò', 'ô', 'ö', 'õ', 'ø'],
        'ss': ['ß'],
        'u': ['ú', 'ù', 'û', 'ü'],
        'A': ['Á', 'À', 'Â', 'Ä', 'Ã', 'Å'],
        'C': ['Ç'],
        'E': ['É', 'È', 'Ê', 'Ë'],
        'I': ['Í', 'Ì', 'Î', 'Ï'],
        'N': ['Ñ'],
        'O': ['Ó', 'Ò', 'Ô', 'Ö', 'ÕØ'],
        'U': ['Ú', 'Ù', 'Û', 'Ü'],
    }
    
    conversao = {}
    for key, value in dict_conversao.items():
        for l in value:
            conversao[l] = key
    for original, novo in conversao.items():
        if not s == None:
            s = s.replace(original, novo)
    return s


def filtrar_string(valor, permitidos='abcdefghijklmnopqrstuvwxyz ,.-0123456789'):
    valor = valor.replace('ç', 'c').replace('Ç', 'c')
    valor = valor.replace('uee', 'ue').replace('üee', 'üe') # catdoc tranforma 'uê' em 'uee' e 'üê' em 'üee'
    filtrado = ''
    for char in del_acento(valor).lower():
        try:
            if not char in permitidos:
                filtrado += ' '
            else:
                filtrado += char
        except:
            filtrado += ' '
    return filtrado


def comeca_com_qualquer_uma(s, lst_strings):
    """
        Retorna True se 's' começar com qualquer uma das strs em 'lst_strings'; retorna False caso contrário
    """
    return any(   filter( lambda x: s.startswith(x), lst_strings )   )


def contem_qualquer_uma(s, lst_strings):
    """
        Retorna True se 's' contiver qualquer uma das strs em 'lst_strings'; retorna False caso contrário
    """
    return any(   filter( lambda x: re.search(x, s), lst_strings )   )


def termina_com_qualquer_uma(s, lst_strings):
    """
        Retorna True se 's' terminar com qualquer uma das strs em 'lst_strings'; retorna False caso contrário
    """
    return any(   filter( lambda x: s.endswith(x), lst_strings )   )


def randomString(string_length=54):
    chars = ascii_letters + digits
    return ''.join( [choice(chars) for i in range(string_length)] )
    
