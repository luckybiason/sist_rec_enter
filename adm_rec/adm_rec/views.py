#-*- coding: utf-8 -*-
from django.shortcuts   import redirect,render
from django.contrib.auth.decorators import login_required
from clientes.models    import Cliente
from lojas.models       import Loja
from televisores.models import Televisor, Marca
from methods            import *

@login_required
def menu(request):
    
    ### -- Estatisticas
    
    # Números
    total_televisores = Televisor.objects.count()
    total_clientes    = Cliente.objects.count()
    total_marcas      = Marca.objects.count()
    total_lojas       = Loja.objects.count()
    
    # Clientes cadastrados
    data_clientes_no_mes  = numero_por_mes_atual("clientes_cliente")
    #data_clientes_no_ano  = numero_por_ano_atual("clientes_cliente")
    
    # Televisores cadastrados
    data_televisores_no_mes  = numero_por_mes_atual("televisores")
    #data_televisores_no_ano  = numero_por_ano_atual("televisores")
    
    #import pdb; pdb.set_trace()
    #datas = [ cli.data_cadastro.month  for cli in clientes ]
    
    return render(request, 'index.html', locals())

def portal(request):
    return redirect('portal.home')

