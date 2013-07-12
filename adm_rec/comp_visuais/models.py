#-*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _ , ugettext_lazy as __
from basiccrud.utils import get_boolean_icon
################################################################################
########################### - CADASTROS AUXILIARES - ########################### 
################################################################################

OPT_LUGAR = (
    ("mis", u"Mista (Chão ou mesa)"),
    ("par", u"Parede"),
    ("cha", u"Chão"),
    ("mes", u"Mesas"),
)

class Categoria(models.Model):
    descricao    = models.CharField(max_length=50, unique=True, verbose_name=__(u"Descrição"))
    lugar        = models.CharField(max_length=3,  choices=OPT_LUGAR, default=OPT_LUGAR[0], verbose_name=__(u"Lugar"))
    sobrepor     = models.BooleanField(default=False, verbose_name=__(u"Permite Sobrepor"))
    is_acento    = models.BooleanField(default=False, verbose_name=__(u"É um acento"))
    is_mesa      = models.BooleanField(default=False, verbose_name=__(u"É uma mesa"))
    is_ponto_luz = models.BooleanField(default=False, verbose_name=__(u"Emite luz/É um ponto de luz"))
    
    class Meta:
        verbose_name        = _(u'categoria')
        verbose_name_plural = _(u'categoria')
        ordering            = ['descricao']

    def __unicode__(self):
        return self.descricao
    
    @models.permalink                                        
    def get_absolute_url(self):                              
       return ('categoria.cadastro', (), {'id': self.id})
   
    def get_lugar(self, obj): return dict(OPT_LUGAR)[self.lugar]
   
    
    @staticmethod
    def get_config():
        return { 
           'titulo'   : _(u"Cadastro de Categorias"),
           'app'      : "categoria",
           'required' : "descricao lugar",
           'js_custom': ["comp_visual_list.js"],
           'fields' : [
                       ('id',        _(u'Cód.'),      True),
                       ('descricao', _(u'Descrição'), False),
                       ('get_lugar', _(u'Lugar'),     False),
                       (lambda obj: get_boolean_icon(obj.is_acento), _(u'Acento'), False),
                       (lambda obj: get_boolean_icon(obj.is_mesa), _(u'Mesa'), False),
                       (lambda obj: get_boolean_icon(obj.is_ponto_luz), _(u'Ponto de Luz'), False),
            ],
        }
    
    @staticmethod
    def success_url(): 
        return "categoria.listagem"

################################################################################
############################ - CADASTRO PRINCIPAL - ############################
################################################################################

'''
class ComponenteVisual(models.Model):
    nome = models.CharField(max_length=50, unique=True, verbose_name=__(u"Nome"))
    nome    Campo de no máximo 45 caracteres    Não pode estar vazio nem duplicado
imagem    Campo do tipo texto    Guarda o caminho da imagem salva no servidor. É obrigatório.
categoria    Campo do tipo inteiro que representa uma chave estrangeira para a tabela Categoria    É obrigatorio.
altura_padrao    campo do tipo real medido em metros. Não poderá ser negativo nem igual a zero    É obrigatorio.
largura_padrao    campo do tipo real medido em metros. Não poderá ser negativo nem igual a zero    É obrigatorio.
is_televisor    Campo do tipo booleano, padrão é false    Indica se o componente é o espaço reservado para o televisor. Somente poderá haver um desses na tabela.

    class Meta:
        verbose_name        = _(u'Componente visual')
        verbose_name_plural = _(u'Componentes visuais')
        ordering            = ['nome']

    def __unicode__(self):
        return self.nome
    
    @models.permalink                                        
    def get_absolute_url(self):                              
       return ('comp_visuais.cadastro', (), {'id': self.id})
   
    @staticmethod
    def success_url(): 
        return "comp_visuais.listagem"
'''    
   