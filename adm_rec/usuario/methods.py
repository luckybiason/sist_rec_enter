#-*- coding: utf-8 -*-
from adm_rec.utils.paginators       import makePaginator
from django.contrib                 import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models     import User
from django.shortcuts               import redirect,render
from forms                          import FormUser
from adm_rec.utils.decorators       import ajax_json_view


##- Recuperação de senha

def do_first_step(request):
    '''
    if request.method == 'POST':
            form = FormRecSenha(request.POST)
            if form.is_valid():
                cpf = form.cleaned_data['cpf']
                candidato = ModelCandidato.objects.only('nome', 'email').filter(cpf=cpf).order_by('-dt_cadastro')[0]
                if valida_email(candidato.email):
                    return redirect(reverse('portal_cand.recuperar_senha') + '?' + urlencode({'cpf': cpf, 'passo': 2}))
                else:
                    return redirect(reverse('portal_cand.recuperar_senha') + '?' + urlencode({'cpf': cpf, 'passo': 4}))
            else:
                form_errors = errorlist_modelform(FormRecSenha, form.errors)
        else:
            form = FormRecSenha()
    '''
    return render(request, 'senha/passo_um.html', locals())

def do_second_step(request):
    '''
    cpf = request.GET.get('cpf', '')
        if not (cpf and ModelCandidato.objects.filter(cpf=cpf).exists()):
            return redirect('portal_cand.recuperar_senha')
        candidato = ModelCandidato.objects.only('email').filter(cpf=cpf).order_by('-dt_cadastro')[0]
        if not valida_email(candidato.email):
            return redirect('portal_cand.recuperar_senha')
        
        FormTipoRecSenha = get_form_tipo_rec_senha(candidato.email)
        if request.method == 'POST':
            form = FormTipoRecSenha(request.POST)
            form_alt_email = FormAltEmail(request.POST)
            
            if form.is_valid():
                tipo = form.cleaned_data['tipo']
                if tipo == '1':
                    enviado = definir_nova_senha(request, candidato, candidato.email)
                    if enviado:
                        mensagem = 'A nova senha foi enviada para o seu email. Clique em "Login" no menu à esquerda para entrar no sistema.'
                    else:
                        mensagem = 'Não foi possível gerar uma nova senha agora. Por favor, tente novamente mais tarde.'
                    return redirect(reverse('portal_cand.recuperar_senha') + '?' + urlencode({'mensagem': mensagem, 'passo': 3}))
                elif tipo == '2':
                    if form_alt_email.is_valid():
                        email_novo = form_alt_email.cleaned_data['email_novo']
                        enviado = definir_nova_senha(request, candidato, email_novo)
                        if enviado:
                            mensagem = 'A nova senha foi enviada para o email "%s". Clique em "Login" no menu à esquerda para entrar no sistema.' % email_novo
                        else:
                            mensagem = 'Não foi possível gerar uma nova senha agora. Por favor, tente novamente mais tarde.'
                        return redirect(reverse('portal_cand.recuperar_senha') + '?' + urlencode({'mensagem': mensagem, 'passo': 3}))
                    else:
                        form_alt_email_errors = errorlist_modelform(FormAltEmail, form_alt_email.errors)
            else:
                form_errors = errorlist_modelform(FormRecSenha, form.errors)
        else:
            form = FormTipoRecSenha()
            form_alt_email = FormAltEmail(initial={'cpf': cpf})
    '''
    return render(request, 'senha/passo_dois.html', locals())

def do_third_step(request):
    return render(request, 'senha/passo_tres.html', locals())

EXECUTAR_PASSO = {
    '1': do_first_step,
    '2': do_second_step,
    '3': do_third_step,
}