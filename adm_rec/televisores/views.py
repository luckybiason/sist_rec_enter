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

