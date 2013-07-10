#-*- coding: utf-8 -*-
from django.utils.encoding    import *
from django.core.urlresolvers import reverse
from methods                  import catch_urls
from django.shortcuts         import render
from django.utils.translation import ugettext as _ , ugettext_lazy as __, ungettext

translate = lambda obj,field : force_unicode(getattr(obj,field), encoding='utf-8', strings_only=False, errors='strict')#.encode('ascii', 'ignore')

### - Funções de HTML Dinâmico - ###

#- Filtros
def _make_filters(qnt,fields,locals,request):
    locals["qnt"]=qnt
    #teste = ungettext( 'Existe %(qntd)s registro', 'Existem %(qntd)s registros', qnt)  % { 'qntd': str(qnt), }
    #locals["teste"]=teste
    return render(request,'grid/filtros.html',locals).content

#- Cabeçalho
def _make_thead(fields,locals,request):
    return render(request,'grid/thead.html', {'fields':fields}).content

#- Opções no final da linha
def _details(request,id,excluir,detail=True):
    return render(request,'grid/opcoes.html', {'excluir':excluir,'id':id,"detail":detail}).content

#- Footer: Paginação 
def _make_tfoot(fields,locals,request):
    locals["cols_num"] = str( int(len(fields)/2)+1 )
    return render(request,'grid/paginacao.html', locals).content


CLASS_DETAIL= "style='display:None' class='detalhes'"
HIDE_DETAIL = "<td "+CLASS_DETAIL+">%s</td>" #Hack para o plugin de ordenação
DETAIL      = "<td colspan='%s' id='datalhes%s' %s></td>"   #Linha do detalhe
    
def _make_body(urls,fields, objetos,request,with_details=True):
    body=""
    cols_num = str( int(len(fields))+2 )
    if objetos:
        for p in objetos:
            linha     = "<tr style='display: table-row;'>"
            linha_det = "<tr><td %s></td>"%CLASS_DETAIL
            for field,label,isLink in fields :
                linha += ("<td>%s</td>" if not isLink else "<td><a href='"+reverse(urls["cadastro"],args=[p.pk])+"'>%s</a></td>")%translate(p,field)
                linha_det += HIDE_DETAIL%translate(p,field)
            linha += _details(request,
                             p.pk,
                             reverse(urls["excluir"],args=[p.pk]),
                             with_details)
            linha += (linha_det+DETAIL%(cols_num,p.pk,CLASS_DETAIL) if with_details else "")
            body  += linha+"</tr>"
    else:
        body = body + "<td colspan='%s'>%s</td> "%(cols_num,_(u"Nenhum registro cadastrado."))
    return "<tbody>%s</tbody>"%(body)

LINE_DETAIL = "<th class='ui-widget-header'>%s:</th><td>%s</td>"

from django.utils.translation import ugettext as _ 
def make_details(model,request):
    obj    = model.objects.get(pk=request.GET['id'])
    fields = model.get_config().get("details_fields","")
    #import pdb;pdb.set_trace()
    if not fields: 
        fields = [ (f.name,f.verbose_name, lambda obj,fi_name: translate(obj,fi_name)) for f in model._meta.fields ]
        
    details = ""
    par     = 0
    for field,label,f in fields :
        if not par: 
            details += "<tr>"
        details+= LINE_DETAIL%(_(label),f(obj,field))
        par    += 1
        if par==2:
            details += "</tr>"
            par     =  0
    return details


##- Função para criação da tabela de listagem
def make_table(request,model,objetos,with_details=True,locals={}):
    '''
       objetos = queryset
       fields = [('id','ID',True),('nome','Nome',False),('telefone','Telefone',True), ... ]
    '''
    qnt    = len(objetos)
    urls   = catch_urls(model)
    fields = model.get_config().get("fields","")
    if not fields: 
        fields = [ (f.name,f.verbose_name,True) for f in model._meta.fields ]
            
    locals["thead"]   = _make_thead(fields,locals,request)
    locals["body"]    = _make_body(urls,fields,objetos,request,with_details)
    locals["tfoot"]   = _make_tfoot(fields,locals,request)
    locals["filters"] = _make_filters(qnt,fields,locals,request)
    
    table = render(request,'grid/table.html',locals).content
    
    return { 'table':table}

