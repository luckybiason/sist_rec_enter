#-*- coding: utf-8 -*-
from clientes.models import Cliente

def id_cliente(request):
    '''
        Esse C.P. injeta o id do cliente 'logado' nos templates do portal.
    '''
    cli = request.session.get("id_cliente", "")
    
    if cli:
        cliente = Cliente.objects.get(pk=cli)
    
    return {
        'ID_CLIENTE': cli,
        'NM_CLIENTE': cliente.nome if cli else None,
    }