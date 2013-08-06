#-*- coding: utf-8 -*-
from django.shortcuts  import render
from methods           import buscar_produtos

#from django.contrib.auth.decorators import login_required
#@login_required
#@user_passes_test(can_make_user)
#can_make_user = lambda u: u.is_superuser or u.is_staff

def home(request):
    return render(request, 'portal/home.html', locals())

def buscar(request):
    ''' Função de busca de produtos no site '''
    produtos = buscar_produtos(request)
    return render(request, 'portal/listagem_produtos.html', locals())