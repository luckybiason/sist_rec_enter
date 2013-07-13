#-*- coding: utf-8 -*-
from adm_rec.utils.decorators import ajax_json_view
from models import Funcao

@ajax_json_view
def getdetail_funcao(request):
    id = request.GET.get('id','')
    if not id:
        return { 'html': u" Função não existe. " }
    funcao = Funcao.objects.get(pk=id)
    return { 'html': u" <b>Descrição:</b> %s " % funcao.descricao }
