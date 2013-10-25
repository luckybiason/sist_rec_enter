#-*- coding: utf-8 -*-
import re
from televisores.models    import Televisor
from adm_rec.utils.sql     import sql_to_dict, sql_escape
from adm_rec.utils.strings import del_acento  

OPERADOR = {
    '+' : ' AND ',
    ' ' : ' OR ',  
}
        
def _definir_key_words(texto, add_clausulas):
    '''
       Entrada, texto digitado pelo usuario no campo de busca
       Saida, clausulas Where para essas palavras chaves
    '''
    def _validando_texto(texto):
        '''
            valida o texto da busca para não dar erros ao usuário
        '''
        # reservados multiplos no inicio
        while True:
            if texto.startswith(' ') or texto.startswith('+'):
                texto = texto[1:]
            else: break
        # reservados multiplos no fim
        while True:
            if texto.endswith(' ') or texto.endswith('+'):
                texto = texto[:-1]
            else: break
        # reservados multiplos no meio
        if re.search('[+| ]{2,}',texto):
            texto = re.sub('[ ]{2,}', ' ', texto)
            texto = re.sub('[+| ]{2,}', '+', texto)
        if re.search('[\"]{2,}',texto):
            texto = re.sub('[\"]{2,}', '\"', texto)
        return texto
    
    # Preparo inicial
    clausulas = []
    texto     = _validando_texto(texto)
    buff      = ''
    aspas     =  False
    char      = ''
    # Algoritmo
    for char in texto:
        if char == '"': # Entra na zona-livre
            aspas = True
            continue
        if aspas: # Zona livre, qualquer caracter vai para o buffer
            buff+=char
            continue
        if not char in ['+',' ']: # Caracter normal
            buff += char # Apenas caracteres normais são colocados no buffer
        else:
            add_clausulas(clausulas, buff, OPERADOR[char]) # Adiciona às clausulas o buffer
            buff = '' #limpa o buffer
    add_clausulas(clausulas, buff, '') # Adiciona o restante do buffer
    # Envolver as clausulas em parênteses
    return "( "+" ".join(clausulas)+" )"

def _wheres_palavras_chave(texto):

    def _adicionar_clausulas_postgresql(lst_clausulas, palavra, operador):
        query_re = "('%(inicio)s' || '%(palavra)s' || '%(fim)s')" % {
            'palavra'  : del_acento(sql_escape(str(palavra))),
            #'palavra'  : palavra,
            'inicio'   : "(\n| |^)",
            'fim'      : "([^A-z]|$|\n)"
        } 
        lst_clausulas.append( """
            (
                del_acento(televisores.nome) ~* %(query_re)s  OR
                del_acento(televisores.especificacao) ~* %(query_re)s  /*OR*/
            )
            %(operador)s """ % {
                'query_re' : query_re,
                'operador' : operador
            } 
        )       
    
    def _adicionar_clausulas_sqllite(lst_clausulas, palavra, operador):
        lst_clausulas.append( """
            (
                televisores.nome like '"""+palavra+"""'  OR
                televisores.especificacao like '"""+palavra+"""'
            )
             """ + operador +" "
        )       
    return _definir_key_words(texto, _adicionar_clausulas_postgresql)
    
def _buscar_televisores(request):
    palavras = request.GET.get('pesq_busca',"")
    wheres   = _wheres_palavras_chave(palavras)
    
    return """
         SELECT televisores.id
         FROM televisores
         """+(" WHERE "+ wheres if wheres else "")+"""
         order by televisores.nome
    """ 

# - Função principal
def buscar_produtos(request):
    televisores = Televisor.objects.raw(_buscar_televisores(request).replace("\n",""))
    return Televisor.objects.filter(pk__in=[ t.id for t in televisores])
    