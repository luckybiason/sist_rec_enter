#-*- coding: utf-8 -*-
from adm_rec.utils.paginators       import makePaginator
from django.contrib                 import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models     import User
from django.shortcuts               import redirect,render
from forms                          import FormUser
from adm_rec.utils.decorators       import ajax_json_view

@ajax_json_view
def getdetail(request):
    return { 'html': u" << Permissões do usuário %s, a implementar >> " % request.GET.get('id','') }

can_make_user = lambda u: u.is_superuser or u.is_staff
TITULO = "Cadastro de Usuários"

@login_required
@user_passes_test(can_make_user)
def usuario_list(request):
    titulo   = TITULO
    usuarios = User.objects.all()
    qnt      = len(usuarios)
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
    titulo = TITULO
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

@login_required
@user_passes_test(can_make_user)
def recuperar_senha(request):
    '''
        1: Cliente digita email ou login
        2: (POST): Gera senha, envia email e redireciona para o passo 3
        3: Concluído
    '''
    passo = request.GET.get('passo', '1')
    if EXECUTAR_PASSO.has_key(passo):
        return EXECUTAR_PASSO[passo](request)
    else:
        messages.error(request, "Passo inválido. Você será direcionado ao primeiro passo.")
        passo= '1'
    return render(request, 'senha/recuperar_senha.html', locals())