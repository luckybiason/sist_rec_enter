#-*- coding: utf-8 -*-
from adm_rec.utils.decorators import ajax_json_view
from adm_rec.utils.paginators import makePaginator
from django.contrib           import messages
from django.shortcuts         import redirect,render
from models                   import *

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
def list_conexoes(request, tel_id):
    #from gridlist import make_table
    #make_table(request, model, object_list, locals=locals)
    conexoes = TelevisorConexao.objects.filter(televisor__id=tel_id)
    num_pag, page, paginator = makePaginator(request,conexoes)
    id_tele = tel_id
    return render(request, 'televisor/cad_conexoes_list.html', locals())

def cad_conexoes(request, tel_id=None):
    id_tele = request.GET.get('id_tele')
    conexoes = TelevisorConexao.objects.filter(televisor__id=tel_id)
    num_pag, page, paginator = makePaginator(request,conexoes)
    return render(request, 'televisor/cad_conexoes_list.html', locals())

def exc_conexoes(request, tel_id):
    id_tele = request.GET.get('id_tele')
    conexoes = TelevisorConexao.objects.filter(televisor__id=tel_id)
    num_pag, page, paginator = makePaginator(request,conexoes)
    return render(request, 'televisor/cad_conexoes_list.html', locals())

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

#- Itens Inclusos
def list_itens(request, tel_id):
    itens = TelevisorConexao.objects.filter(televisor__id=tel_id)
    num_pag, page, paginator = makePaginator(request,itens)
    return render(request, 'televisor/cad_itens_list.html', locals())

#- Lojas
def list_lojas(request, tel_id):
    lojas = TelevisorLoja.objects.filter(televisor__id=tel_id)
    num_pag, page, paginator = makePaginator(request,lojas)
    return render(request, 'televisor/cad_lojas_list.html', locals())
