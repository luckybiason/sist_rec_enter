#-*- coding: utf-8 -*-
from adm_rec.utils.decorators import ajax_json_view
from django.shortcuts         import redirect,render
from lojas.models             import Loja
from methods_busca            import buscar_produtos
from televisores.models       import Televisor, Marca, TelevisorLoja, TelevisorConexao, TelevisorItens
from portal.models            import Comentario

#from django.contrib.auth.decorators import login_required
#@login_required
#@user_passes_test(can_make_user)
#can_make_user = lambda u: u.is_superuser or u.is_staff

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
    conexoes  = TelevisorConexao.objects.filter(televisor=televisor)
    itens     = TelevisorItens.objects.filter(televisor=televisor)
    coments   = Comentario.objects.filter(televisor=televisor)
    
    return render(request, 'portal/produtos/detalhes_televisores.html', locals())

@ajax_json_view
def salvar_comentario(request):
    ''' Função que salva o comentário de um televisore '''
    
    id_televisor = request.GET.get('id_televisor','')
    if not id_televisor:
        return { 'erro' : 'Sem televisor' }    
    televisor = Televisor.objects.get(pk=id_televisor)
    
    nome = request.GET.get('nome','')
    if not nome:
        return { 'erro' : 'Por favor, preencha o nome.' }  
    
    comentario = request.GET.get('comentario','')
    if not comentario:
        return { 'erro' : 'Por favor, preencha o comentário.' }  
    
    try:
        comnt = Comentario()
        comnt.televisor  = televisor
        comnt.nome       = nome
        comnt.comentario = comentario
        comnt.nota       = int(request.GET.get('nota','0'))
        comnt.save()
    except Exception, ex:
        print ex
        return {'erro' : ex }
    return { 'status' : 'Comentário Salvo com sucesso' }  

@ajax_json_view
def lista_comentarios(request):
    ''' Função que lista os comentários de um televisor '''
    
    id_televisor = request.GET.get('id_televisor','')
    if not id_televisor:
        return { 'erro' : 'Sem televisor' }    
    
    coments   = Comentario.objects.filter(televisor__id=id_televisor)
    return { 'coments' : [ { 'id':c.id, 'data':str(c.data), 'nome':c.nome, 'comentario':c.comentario, 'nota':c.nota} for c in coments ] }
    