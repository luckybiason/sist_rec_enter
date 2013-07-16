#-*- coding: utf-8 -*-
from adm_rec.utils.decorators       import ajax_json_view
from models import ComponenteVisual

HTML_DETAIL_CV = lambda comp_visual: '''
<table cellspacing='4px' cellpadding='4px' style='margin-left: auto; margin-right: auto; border:none!important;'>
    <tr>
        <td rowspan='3' style='vertical-align: middle;' width='300px'>
         %(imagem)s
        </td>
        <th>Categoria:</th>
        <td>%(categoria)s</td>
    </tr>
    <tr>
        <th>Largura:</th>
        <td>%(largura)s</td>
    </tr>
    <tr>
        <th>Altura:</th>
        <td>%(altura)s</td>
    </tr>
</table>
''' % { 
   'imagem'   : comp_visual.get_imagem(),
   'categoria': comp_visual.categoria,
   'altura'   : comp_visual.altura_padrao,
   'largura'  : comp_visual.largura_padrao
}

@ajax_json_view
def getdetail_comp_visuais(request):
    id  = request.GET.get('id','')
    if not id:
        return { 'html': u"  " }
    comp_visual = ComponenteVisual.objects.filter(pk=id)[0]
    return { 'html': u" %s " % HTML_DETAIL_CV(comp_visual) }
