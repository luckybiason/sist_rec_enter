#-*- coding: utf-8 -*-
from adm_rec.utils.decorators import ajax_json_view
from models import Funcao, Televisor

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



from basiccrud.views import *

## - Views dos televisores
#cad_televisor = GeneralCreateView.as_view(model=Televisor, template_name='televisor/cadastro.html')
#upd_televisor = GeneralUpdateView.as_view(model=Televisor, template_name='televisor/cadastro.html')

class Cad_televisor(GeneralCreateView):
    def after_post(self, request):
        print request

cad_televisor = Cad_televisor.as_view(model=Televisor, template_name='televisor/cadastro.html')

#def teste(self, request):
#        print "request"
#cad_televisor = GeneralCreateView.as_view(after_post=teste,
#                                          model=Televisor, 
#                                          template_name='televisor/cadastro.html')

class Upd_televisor(GeneralUpdateView):
    def after_post(self, request):
        print "request"
upd_televisor = Upd_televisor.as_view(model=Televisor, template_name='televisor/cadastro.html')

