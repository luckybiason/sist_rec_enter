#-*- coding: utf-8 -*-
from django.shortcuts import redirect,render
from methods_busca    import buscar_produtos

#from django.contrib.auth.decorators import login_required
#@login_required
#@user_passes_test(can_make_user)
#can_make_user = lambda u: u.is_superuser or u.is_staff

from televisores.models import Televisor, Marca, TelevisorLoja
from lojas.models import Loja
def home(request):
    # Principais televisores
    televisores = Televisor.objects.all()
    # Principais marcas
    marcas = Marca.objects.all()
    # Principais lojas
    lojas = Loja.objects.all()
    for loja in lojas:
        loja.quantidade_prod = len(TelevisorLoja.objects.filter(loja=loja))
    return render(request, 'portal/home.html', locals())

def buscar(request):
    ''' Função de busca de produtos no site '''
    produtos = buscar_produtos(request)
    return render(request, 'portal/listagem_produtos.html', locals())

def visualizar(request, id_televisor):
    ''' Função que carrega um televisor e seus detalhes '''
    
    if not id_televisor:
        return redirect('usuario.listagem')
    
    televisor = Televisor.objects.get(pk=id_televisor)
    lojas     = TelevisorLoja.objects.filter(televisor=televisor)
    
    return render(request, 'portal/produtos/detalhes_televisores.html', locals())
