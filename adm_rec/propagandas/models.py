#-*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _ , ugettext_lazy as __
from django.core.urlresolvers import reverse
from lojas.models import Loja
from basiccrud.utils import get_boolean_icon

class Propaganda(models.Model):
    imagem        = models.ImageField(upload_to='img_prop', blank=True, null=True, verbose_name=__(u"Banner:"))
    loja          = models.ForeignKey(Loja, verbose_name=__(u"Loja:"))
    ordem         = models.IntegerField(verbose_name=__(u"Ordem:"))
    is_ativo      = models.BooleanField(verbose_name=__(u"Ativo?"), blank=True, default=False)
    data_cadastro = models.DateField(verbose_name=__(u"Data cadastro"), auto_now=True)
    dias_expira   = models.IntegerField(verbose_name=__(u"Dias que expiram:"), default=1)
    
    class Meta:
        verbose_name        = _(u'propaganda')
        verbose_name_plural = _(u'propagandas')
        ordering            = ['ordem']

    def __unicode__(self):
        return " propaganda da loja "+str(self.loja)
    
    @models.permalink                                        
    def get_absolute_url(self):                   
       return ('propagandas.cadastro', (), {'id': self.id})
   
    def get_imagem(self, obj): 
        return u'''<img src='/media/%s' width='50px'>''' % str(self.imagem)
    
    def get_ativo(self, obj):
        return get_boolean_icon(self.is_ativo)
    
    @staticmethod
    def get_config():
        return { 
           'titulo'   : _(u"Cadastro de propagandas"),
           'app'      : "propagandas",
           'required' : "ordem dias_expira loja",
           'fields' : [
                       ('id',            _(u'Cód.'),             True),
                       ('data_cadastro', _(u'Data de cadastro'), False),
                       ('loja',          _(u'Loja'),             False),
                       ('dias_expira',   _(u'Dias Expira'),      True),
                       ('get_ativo',      _(u'Ativa'),            True),
            ],
        }
    
    @staticmethod
    def success_url(): 
        return "propagandas.listagem"
   