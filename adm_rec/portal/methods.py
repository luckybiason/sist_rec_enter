#-*- coding: utf-8 -*-
from clientes.models import Cliente

def get_cliente_from_session(request):
    if request.session.get("id_cliente", ""):
        return Cliente.objects.get(pk=request.session.get("id_cliente"))
    return None