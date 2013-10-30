#-*- coding: utf-8 -*-
from adm_rec.utils.decorators import ajax_json_view
from adm_rec.utils.paginators import makePaginator
from clientes.models          import Cliente
from django.shortcuts         import redirect,render
from filtragem.models         import USOS_CHOICES
from lojas.models             import Loja
from methods                  import get_cliente_from_session
from methods_busca            import buscar_produtos
from portal.models            import Comentario
from portal.methods_filtros   import selecionar, filtrar as filtrar_produtos, prepare, get_filtros
from propagandas.models       import Propaganda
from recomendacao.methods     import recomendar
from televisores.models       import Televisor, Marca, TelevisorLoja, TelevisorConexao, TelevisorItens

def home(request):    
    # Principais marcas
    marcas = Marca.objects.all()
    
    # Principais lojas
    lojas = Loja.objects.all()
    for loja in lojas:
        loja.quantidade_prod = len(TelevisorLoja.objects.filter(loja=loja))
        
    # Propagandas
    propagandas = Propaganda.objects.filter(is_ativo=True)
    
    # Informações para a filtragem
    usos = USOS_CHOICES
        
    # Gerar recomendados/principais
    cliente = get_cliente_from_session(request)
    if cliente:
        # Recomendados
        recomendados = recomendar(cliente)
    
    # Principais televisores
    televisores = Televisor.objects.all()
    
    return render(request, 'portal/home.html', locals())

def visualizar(request, id_televisor):
    ''' Função que carrega um televisor e seus detalhes '''
    
    if not id_televisor:
        return redirect('usuario.listagem')
    
    televisor = Televisor.objects.get(pk=id_televisor)
    televisor = prepare(request, [televisor])[0]
    lojas     = TelevisorLoja.objects.filter(televisor=televisor)
    conexoes  = TelevisorConexao.objects.filter(televisor=televisor)
    itens     = TelevisorItens.objects.filter(televisor=televisor)
    coments   = Comentario.objects.filter(televisor=televisor)
    qntde_coments = len(coments)
    
    televisor.nota5 = coments.filter(nota=5).count()
    televisor.nota4 = coments.filter(nota=4).count()
    televisor.nota3 = coments.filter(nota=3).count()
    televisor.nota2 = coments.filter(nota=2).count()
    televisor.nota1 = coments.filter(nota=1).count()
        
    # Aplicar visita
    cliente = get_cliente_from_session(request)
    televisor.adicionar_visita(cliente)
    
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
    
    # Se cliente logado, o comentário pertence a ele
    cliente = None
    if request.session.get("id_cliente", ""):
        cliente = Cliente.objects.get(pk=request.session.get("id_cliente"))
        nome    = cliente.nome
    #####################################################################
    
    try:
        comnt = Comentario()
        comnt.televisor  = Televisor.objects.get(pk=id_televisor)
        comnt.nome       = nome
        comnt.comentario = comentario
        comnt.cliente    = cliente
        comnt.nota       = int(request.GET.get('nota','1'))
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
    
    ## Paginação e Informações adicionais
    num_pag, page, paginator = makePaginator(request,produtos,group=8)
    page.object_list = prepare(request, page.object_list)
    
    ## Informações para filtragem
    marcas, precos, telas, informacoes = get_filtros(request, produtos)
    produtos = prepare(request, produtos)
    ## Cache
    id_produtos = ",".join( [ str(obj.id) for obj in produtos] )
    pl_chave = request.GET.get("pesq_busca","")
    
    return { 'html' : render(request, 'portal/vitrine/vitrine_produtos.html', locals()).content }