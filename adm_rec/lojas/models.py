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
    
    @models.permalink                                        
    def get_absolute_url(self):                              
       return ('loja.cadastro', (), {'id': self.id})
   
    def show_logo(self):
        return '''<img src='%(img)s' heigth='50px'>''' % self.logo
   
    @staticmethod
    def get_config():
        return { 
           'titulo'   : _(u"Cadastro de Lojas"),
           'app'      : "lojas",
           'required' : "nome",
           'fields' : [
                       ('id',   _(u'Cód.'), True),
                       ('nome', _(u'Nome'), False) 
            ],
        }
    
    @staticmethod
    def success_url(): 
        return "loja.listagem"