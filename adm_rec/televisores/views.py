#-*- coding: utf-8 -*-
from adm_rec.utils.decorators import ajax_json_view
from adm_rec.utils.paginators import makePaginator
from django.contrib           import messages
from django.shortcuts         import redirect,render
from models                   import *
from django.http import HttpResponseRedirect

@ajax_json_view
def getdetail_funcao(request):
    id = request.GET.get('id','')
    if not id:
        return { 'html': u" Função não existe. " }
    funcao = Funcao.objects.get(pk=id)
    return { 'html': u" <b>Descrição:</b> %s " % funcao.descricao }


@ajax_json_view
def getdetail_televisor(request):
    id  = request.GET.get('id','')
    if not id:
        return { 'html': u"  " }
    tele = Televisor.objects.filter(pk=id)[0]
    return { 'html': u" %s " % str(tele) }


##-- Funções dos relacionamentos de Televisores

#- Conexoes
from models import TelevisorConexao
from forms  import TelevisorConexaoForm

def list_conexoes(request):
    titulo   = "Listagem de conexões"
    id_tele  = request.GET.get('id_tele')
    conexoes = TelevisorConexao.objects.filter(televisor__id=id_tele)
    num_pag, page, paginator = makePaginator(request,conexoes)
    return render(request, 'televisor/cad_conexoes_list.html', locals())

def cad_conexoes(request, pk=None):
    titulo  = "Cadastro de conexões"
    
    if request.method =='POST':
        id_tele = request.POST.get('televisor')
    else:
        id_tele = request.GET.get('id_tele')
        
    if request.method =='POST':
        if pk:
            tvcon = TelevisorConexao.objects.get(id=pk)
            form  = TelevisorConexaoForm(request.POST,instance=tvcon)
        else:
            form = TelevisorConexaoForm(request.POST)
        if form.is_valid():
            tvcon = form.save()
            messages.success(request, 'A conexão foi salva com sucesso')
            return redirect(reverse('conexoes.listagem')+'?id_tele=%s' % id_tele)
        else:
            if TelevisorConexao.objects.filter(televisor__id=id_tele,
                                         conexao__id=request.POST.get('conexao')).exists():
                messages.error(request, u'Já existe uma conexão dessas para o televisor.')
            else:
                messages.error(request, u'Existem erros de preenchimento no formulário.')
    else:
        if pk:
            tvcon = TelevisorConexao.objects.get(id=pk)
            form  = TelevisorConexaoForm(instance=tvcon)
        else:
            form = TelevisorConexaoForm()
    return render(request, 'televisor/cad_conexoes_form.html', locals())

def exc_conexoes(request, pk):
    titulo  = "Exclusão da conexão inclusa no televisor"
    id_tele = request.GET.get('id_tele')
    conexao = TelevisorConexao.objects.get(id=pk)
    if request.method == 'POST':
        conexao.delete()
        return redirect(reverse('conexoes.listagem')+'?id_tele=%s' % id_tele)
    return render(request, 'televisor/cad_conexoes_exc.html', locals())

#- Itens Inclusos
from models import TelevisorItens
from forms  import TelevisorItensForm

def list_itens(request):
    titulo   = "Listagem de itens inclusos"
    id_tele  = request.GET.get('id_tele')
    itens    = TelevisorItens.objects.filter(televisor__id=id_tele)
    num_pag, page, paginator = makePaginator(request,itens)
    return render(request, 'televisor/cad_itens_list.html', locals())

def cad_itens(request, pk=None):
    titulo  = "Cadastro de itens inclusos no televisor"
    
    if request.method =='POST':
        id_tele = request.POST.get('televisor')
    else:
        id_tele = request.GET.get('id_tele')
        
    if request.method =='POST':
        if pk:
            tvcon = TelevisorItens.objects.get(id=pk)
            form  = TelevisorItensForm(request.POST,instance=tvcon)
        else:
            form = TelevisorItensForm(request.POST)
        if form.is_valid():
            tvcon = form.save()
            messages.success(request, 'o item foi salvo com sucesso')
            return redirect(reverse('tel_itens.listagem')+'?id_tele=%s' % id_tele)
        else:
            if TelevisorItens.objects.filter(televisor__id=id_tele,
                                                  item__id=request.POST.get('item')).exists():
                messages.error(request, u'Já existe um item desse para o televisor.')
            else:
                messages.error(request, u'Existem erros de preenchimento no formulário.')
    else:
        if pk:
            tvcon = TelevisorItens.objects.get(id=pk)
            form  = TelevisorItensForm(instance=tvcon)
        else:
            form = TelevisorItensForm()
    return render(request, 'televisor/cad_itens_form.html', locals())

def exc_itens(request, pk):
    titulo  = "Exclusão do item incluso no televisor"
    id_tele = request.GET.get('id_tele')
    item = TelevisorItens.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect(reverse('tel_itens.listagem')+'?id_tele=%s' % id_tele)
    return render(request, 'televisor/cad_itens_exc.html', locals())

#- Lojas
from models import TelevisorLoja
from forms  import TelevisorLojaForm

def list_lojas(request):
    titulo   = "Listagem de lojas"
    id_tele  = request.GET.get('id_tele')
    lojas    = TelevisorLoja.objects.filter(televisor__id=id_tele)
    num_pag, page, paginator = makePaginator(request,lojas)
    return render(request, 'televisor/cad_lojas_list.html', locals())

def cad_lojas(request, pk=None):
    titulo  = "Cadastro de lojas do televisor"
    
    if request.method =='POST':
        id_tele = request.POST.get('televisor')
    else:
        id_tele = request.GET.get('id_tele')
        
    if request.method =='POST':
        if pk:
            tvcon = TelevisorLoja.objects.get(id=pk)
            form  = TelevisorLojaForm(request.POST,instance=tvcon)
        else:
            form = TelevisorLojaForm(request.POST)
        if form.is_valid():
            tvcon = form.save()
            messages.success(request, 'A loja foi anexada ao televisor com sucesso')
            return redirect(reverse('tel_lojas.listagem')+'?id_tele=%s' % id_tele)
        else:
            if TelevisorLoja.objects.filter(televisor__id=id_tele,
                                                 loja__id=request.POST.get('loja')).exists():
                messages.error(request, u'Já existe uma loja dessa para o televisor.')
            else:
                messages.error(request, u'Existem erros de preenchimento no formulário.')
    else:
        if pk:
            tvcon = TelevisorLoja.objects.get(id=pk)
            form  = TelevisorLojaForm(instance=tvcon)
        else:
            form = TelevisorLojaForm()
    return render(request, 'televisor/cad_lojas_form.html', locals())

def exc_lojas(request, pk):
    id_tele = request.GET.get('id_tele')
    return render(request, 'televisor/cad_lojas_list.html', locals())



#from basiccrud.views import *
#class ConexoesListView(GeneralListView):
#    def get_queryset(self):
#        if self.request.GET.get('obj_id',''):
#            return TelevisorConexao.objects.filter(televisor__id=self.request.GET['obj_id'])
#        else:
#            return TelevisorConexao.objects.all()
#list_conexoes = ConexoesListView.as_view(model=TelevisorConexao, 
#                                         template_base='iframe.html',
#                                         template_name='cad_conexoes_list.html')
