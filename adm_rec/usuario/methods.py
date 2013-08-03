#-*- coding: utf-8 -*-
from adm_rec.utils.paginators       import makePaginator    
from django.contrib                 import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models     import User
from django.shortcuts               import redirect,render
from forms                          import FormUser
from adm_rec.utils.decorators       import ajax_json_view
from senhas                         import gerar_senha, cria_hash      
from adm_rec.utils.emails           import envia_email

##- Recuperação de senha
EMAIL_TEXTO = lambda senha_nova, user : u'''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<head>

<meta http-equiv="content-type" content="text/html; charset=utf-8" charset='utf-8'>
</head>

<body>
    <img src="%(logo)s"  height="150px"/>
    <p>
        <hr>
        Prezado(a) %(nome)s,
        <br/>
        <br/>
        Você solicitou a troca de senha no sistema administrador.
        <br/>
        Seu login é: <b>%(login_usu)s</b>
        <br/>
        Sua nova senha é: <b>%(senha_nova)s</b>
        <br/>
        <br/>
        Obrigado.
        Administração do No Alvo
        <hr>
    </p>

</body>
</html>
''' % {  
    'link'      : '',
    'logo'      : '',
    'senha_nova': senha_nova,
    'login_usu' : user.username,
    'nome'      : user.first_name,
}


def do_first_step(request):
    prox_passo = '2'
    template   = 'senha/passo_um.html'
    return render(request, 'senha/recuperar_senha.html', locals())

def do_second_step(request):
    prox_passo = '3'
    template   = 'senha/passo_dois.html'
    username   = request.POST.get('username','')
    user       = User.objects.get(username=username)
    if not user.email:
        messages.error(request, u'Você não tem email válido. Contate o Administrador do sistema para cadastrar uma email válido.')
        return redirect('usuario.recuperar_senha')
    return render(request, 'senha/recuperar_senha.html', locals())

def do_third_step(request):
    template   = 'senha/passo_tres.html'
    # Pega usuario
    username   = request.POST.get('username','')
    user       = User.objects.get(username=username)
    # Cria nova senha
    nova_senha    = gerar_senha(qtd_caracteres=7)
    user.password = cria_hash(nova_senha)
    user.save()
    # Envia email
    envia_email('Recuperação de Senha No Alvo', 
                EMAIL_TEXTO(nova_senha, user),
                [user.email])
    return render(request, 'senha/recuperar_senha.html', locals())

EXECUTAR_PASSO = {
    '1': do_first_step,
    '2': do_second_step,
    '3': do_third_step,
}