#-*- coding: utf-8 -*-
from adm_rec.utils.paginators       import makePaginator
from django.contrib                 import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models     import User
from django.shortcuts               import redirect,render
from forms                          import FormUser

can_make_user = lambda u: u.is_superuser or u.id_staff

@login_required
@user_passes_test(can_make_user)
def usuariodel(request,id):
    usuario = User.objects.get(pk=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario.listagem')
    return render(request, 'usuarios/excluir.html', locals())

@login_required
@user_passes_test(can_make_user)
def usuario_list(request):
    usuarios = User.objects.all()
    num_pag, page, paginator = makePaginator(request,usuarios)
    return render(request, 'usuarios/listagem.html', locals())

import pytz
from datetime import datetime
def populate_user(user, post):
    user.first_name   = post.get('first_name','')
    user.last_name    = post.get('last_name','')
    user.email        = post.get('email','')
    user.is_superuser = post.get('is_superuser','')
    user.is_staff     = post.get('is_staff','')
    user.date_joined  = datetime.now(pytz.utc)
    user.save()

@login_required
@user_passes_test(can_make_user)
def usuario(request, id=None):
    if request.method == 'POST':
        try:
            if id: # Alteração
                user = User.objects.get(id=id)
                form = FormUser(instance= User.objects.get(id=id) )
                populate_user(User.objects.get(id=id), request.POST)
            else: # Criação
                form = FormUser()
                user = User.objects.create_user( username=request.POST['username'],
                                                 password=request.POST['password'],
                                                 email=request.POST['email'] )
                populate_user(user, request.POST)
            messages.success(request,'- O %s foi cadastrado com sucesso' % user.username)
            return redirect('usuario.listagem')
        except Exception, ex:
            messages.error(request,ex)
    else:
        if id:
            form = FormUser(instance= User.objects.get(id=id) )
        else:
            form = FormUser()
    
    return render(request, 'usuarios/cadastro.html', locals())
