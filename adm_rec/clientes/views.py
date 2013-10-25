#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib            import messages
from django.shortcuts          import redirect,render
from forms                     import ClienteForm, ClienteLoginForm
from models                    import Cliente

def cadastro(request):    
    if request.method =='POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cli = form.save()
            messages.success(request, 'O seu cadastro foi efetuado com sucesso')
            request.session["id_cliente"] = cli.id
            return redirect('/')
        else:
            messages.error(request, u'Existem erros de preenchimento no formulário.')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cadastro.html', locals())

def login(request):    
    if request.method =='POST':
        form = ClienteLoginForm(request.POST)
        if form.is_valid():
            cli = form.cleaned_data
            ## - Validar email
            if not Cliente.objects.filter(email=cli['login']).exists():
                messages.error(request, u'Não existe registro cadastrado com esse email. Cadastre-se ou tente outro email.')
            else:    
                ## - Recuperar cadastro
                cliente = Cliente.objects.get(email=cli['login'])
                ## - Validar senha
                if not cli["senha"]==cliente.senha:
                    messages.error(request, u'Senha Inválidal.')
                else:
                    ## - Autenticar e redirecionar
                    request.session["id_cliente"] = cliente.id
                    return redirect('/')
        else:
            messages.error(request, u'Existem erros de preenchimento no formulário.')
    else:
        form = ClienteLoginForm()
    return render(request, 'clientes/login.html', locals())


def logout(request):    
    request.session["id_cliente"] = ''
    return redirect('/')
