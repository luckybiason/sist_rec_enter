#-*- coding: utf-8 -*-
from django.shortcuts  import render
from methods_busca   import buscar_produtos

#from django.contrib.auth.decorators import login_required
#@login_required
#@user_passes_test(can_make_user)
#can_make_user = lambda u: u.is_superuser or u.is_staff

from televisores.models import Televisor, Marca

def home(request):
    # Principais televisores
    televisores = Televisor.objects.all()
    # Principais marcas
    marcas = Marca.objects.all()
    # Principais lojas
    return render(request, 'portal/home.html', locals())

def buscar(request):
    ''' Função de busca de produtos no site '''
    produtos = buscar_produtos(request)
    return render(request, 'portal/listagem_produtos.html', locals())