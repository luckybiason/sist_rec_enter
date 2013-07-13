#-*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _ , ugettext_lazy as __

class Loja(models.Model):
    nome = models.CharField(max_length=50, unique=True, verbose_name=__(u"Nome"))
    logo = models.ImageField(upload_to='img_lojas', blank=True, null=True)
    site = models.CharField(max_length=150, unique=True, verbose_name=__(u"Site"))
    
    class Meta:
        verbose_name        = _(u'Loja')
        verbose_name_plural = _(u'Lojas')
        ordering            = ['nome']

    def __unicode__(self):
        return self.nome
    
    def get_logo(self, obj): 
        return u'''<img src='/media/%s' width='20px'>''' % str(self.logo)
    
    def get_site(self, obj): 
        return u'''<a href='%s'><img src='/static/imagem/web.png' width='20px' title='Ir ao Site' align='absmiddle'>Ir ao Site</a>''' % str(self.site)
    
    @models.permalink                                        
    def get_absolute_url(self):                              
       return ('lojas.cadastro', (), {'id': self.id})
       
    @staticmethod
    def get_config():
        return { 
           'titulo'   : _(u"Cadastro de Lojas"),
           'app'      : "lojas",
           'required' : "nome",
           'fields' : [
                       ('get_logo', _(u'Logo'), True),
                       ('id',   _(u'Cód.'), False),
                       ('nome', _(u'Nome'), False),
                       ('get_site', _(u'Site'), False),
            ],
        }
    
    @staticmethod
    def success_url(): 
        return "lojas.listagem"