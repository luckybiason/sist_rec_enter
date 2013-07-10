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

from datetime import date
@login_required
@user_passes_test(can_make_user)
def usuario(request, id=None):
    today = date.today()
    today = today.strftime('%Y-%m-%d %H:%M:%S')
    print today
    if request.method == 'POST':
        if id:
            u = User.objects.get(id=id)
            form = FormUser(request.POST,request.FILES,instance=u)
        else:
            form = FormUser(request.POST,request.FILES)
            
        if form.is_valid():
            u = form.save()
            messages.success(request,'- O usuário %s foi cadastrado com sucesso' % u.username)
            return redirect(u)
        else: print form.errors
    else:
        if id:
            u = User.objects.get(id=id)
            form = FormUser(instance=u)
        else:
            form = FormUser()
    
    return render(request, 'usuarios/cadastro.html', locals())
