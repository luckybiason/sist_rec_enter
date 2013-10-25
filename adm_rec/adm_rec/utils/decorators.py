# -*- coding: utf-8 -*-

from django.conf import settings

from django.db import connections
from django.http import HttpResponse, HttpResponseForbidden
from django.utils import simplejson

JSON_MIME_TYPE = "application/json"
to_json = simplejson.dumps

def ajax_json_view(view_original):
    """
        Decorator para views ajax que retornam dados em JSON.
        A view decorada deve retornar os dados em Python; este
        decorator cuida do processo de serialização.
    """
    def nova_view(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseForbidden("Acesso Negado!")
        
        dados = view_original(request, *args, **kwargs)
        return HttpResponse(to_json(dados), JSON_MIME_TYPE)
    
    nova_view.__doc__ = view_original.__doc__
    nova_view.__name__= view_original.__name__
    
    return nova_view


def print_sqls(view_original):
    """
        Imprime no Terminal todos os comandos SQL utilizados no processamento da view.
    """
    
    class cores:
        VERMELHO = '\033[91m'
        VERDE = '\033[92m'
        AZUL = '\033[94m'
        CIANO = '\033[96m'
        BRANCO = '\033[97m'
        AMARELO = '\033[93m'
        ROSA = '\033[95m'
        CINZA = '\033[90m'
        PRETO = '\033[90m'
        PADRAO = '\033[99m'
    
    def nova_view(request, *args, **kwargs):
        recuo = ' ' * 4
        
        for id_banco in settings.DATABASES:
            connections[id_banco].queries = []
            
        resposta = view_original(request, *args, **kwargs)
        
        for id_banco in settings.DATABASES:
            if not len(connections[id_banco].queries):
                continue
            
            print '\n'
            print cores.AMARELO
            print '%s%s' % (recuo, '='*50)
            print '%s|   BANCO: %s' % (recuo, id_banco)
            print '%s%s' % (recuo, '='*50)
            print cores.PADRAO,
            
            for q in connections[id_banco].queries:
                print '\n%s%s[%s] %s%s%s' % (
                    recuo,
                    cores.VERDE,
                    q['time'],
                    cores.CIANO,
                    q['sql'],
                    cores.PADRAO
                )
            print cores.AMARELO,
            print '\n%s%s' % (recuo, '='*50)
            print '%s|   Total de queries: %s' % (recuo, len(connections[id_banco].queries))
            print '%s%s\n' % (recuo, '='*50)
            print cores.PADRAO,
        return resposta
    return nova_view