#-*- coding: utf-8 -*-

OPERADOR = {
    '+' : ' AND ',
    ' ' : ' OR ',            
}

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
        
def _definir_key_words(texto, add_clausulas):
    '''
       Entrada, texto digitado pelo usuario no campo de busca
       Saida, clausulas Where para essas palavras chaves
    '''
    # Preparo inicial
    clausulas = []
    texto     = _validando_texto(texto)
    buff      = ''
    aspas     =  False
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
    add_clausulas(clausulas, buff, OPERADOR[char]) # Adiciona o restante do buffer
    # Envolvver as clausulas em parênteses
    return "(%s)" % (" ".join(clausulas))

def _wheres_palavras_chave(texto):

    def _adicionar_clausulas(lst_clausulas, palavra, operador):
        query_re = "('%(inicio)s' || '%(palavra)s' || '%(fim)s')" % {
            'palavra'  : del_acento(sql_escape(palavra)),
            'inicio'   : "(\n| |^)",
            'fim'      : "([^A-z]|$|\n)"
        } 
        lst_clausulas.append( """
            (
                televisores.especificacao ~* %(query_re)s  /*OR*/
            )
            %(operador)s """ % {
                'query_re': query_re,
                'operador' : operador
            } 
        )       
    
    return _definir_key_words(texto, _adicionar_clausulas)
    
def _buscar_televisores(request):
    palavras = request.POST('pesq_busca')
    wheres = _wheres_palavras_chave(texto)
    
    SQL = """
         SELECT televisor.id
         FROM televisor
         %(where)s
         order by televisor.nome
    """ % {
           'where' : " WHERE "+ wheres if wheres else "",
    }
    
    return SQL


# - Função principal
def buscar_produtos(request):
    televisores = buscar_televisores(request)
    # produto = buscar_produto(request) # para outros tipos
    return televisores
    