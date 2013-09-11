#-*- coding: utf-8 -*-
from adm_rec.utils.decorators import ajax_json_view
from django.shortcuts         import redirect,render
from lojas.models             import Loja
from methods_busca            import buscar_produtos
from televisores.models       import Televisor, Marca, TelevisorLoja, TelevisorConexao, TelevisorItens
from propagandas.models       import Propaganda
from portal.models            import Comentario
from adm_rec.utils.paginators import makePaginator
from portal.methods_filtros   import selecionar, filtrar as filtrar_produtos, prepare, get_filtros

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
        
    # Propagandas
    propagandas = Propaganda.objects.filter(is_ativo=True)
    
    return render(request, 'portal/home.html', locals())

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
    
    ### Validações, ocorrem pois é um cadastro Ajax sem formulário  ###
    id_televisor = request.GET.get('id_televisor','')
    if not id_televisor:
        return { 'erro' : 'Sem televisor' }   
    
    nome = request.GET.get('nome','')
    if not nome:
        return { 'erro' : 'Por favor, preencha o nome.' }  
    
    comentario = request.GET.get('comentario','')
    if not comentario:
        return { 'erro' : 'Por favor, preencha o comentário.' }  
    #####################################################################
    
    try:
        comnt = Comentario()
        comnt.televisor  = Televisor.objects.get(pk=id_televisor)
        comnt.nome       = nome
        comnt.comentario = comentario
        comnt.nota       = int(request.GET.get('nota','0'))
        comnt.save()
    except Exception, ex:
        return {'erro' : 'Ocorreu um erro, favor, tente mais tarde.' }
    
    return { 'status' : 'Comentário Salvo com sucesso' }  

@ajax_json_view
def lista_comentarios(request):
    ''' Função que lista os comentários de um televisor '''
    
    id_televisor = request.GET.get('id_televisor','')
    if not id_televisor:
        return { 'erro' : 'Sem televisor' }    
    
    coments   = Comentario.objects.filter(televisor__id=id_televisor)
    return { 'coments' : [ { 'id'        : c.id, 
                             'data'      : str(c.data), 
                             'nome'      : c.nome, 
                             'comentario': c.comentario, 
                             'nota'      : c.nota} for c in coments ] }
    
@ajax_json_view
def filtrar(request):   
        
    ## Seleção e filtragem
    produtos = selecionar(request)
    produtos = filtrar_produtos(request, produtos)
    
    ## Cache
    #id_produtos = ",".join( [ str(obj.id) for obj in produtos] )
    
    ## Paginação e Informações adicionais
    num_pag, page, paginator = makePaginator(request,produtos,group=8)
    page.object_list = prepare(request, page.object_list)
    
    ## Informações para filtragem
    marcas, precos, telas, informacoes = get_filtros(request, produtos)
    
    return { 'html' : render(request, 'portal/vitrine/vitrine_produtos.html', locals()).content }