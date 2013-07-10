#-*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _ , ugettext_lazy as __

################################################################################
########################### - CADASTROS AUXILIARES - ########################### 
################################################################################

class TipoTela(models.Model):
    descricao = models.CharField(max_length=50, unique=True, verbose_name=__(u"Descrição"))
    
    class Meta:
        verbose_name        = _(u'tipo de tela')
        verbose_name_plural = _(u'tipos de tela')
        ordering            = ['descricao']

    def __unicode__(self):
        return self.descricao
    
    @models.permalink                                        
    def get_absolute_url(self):                              
       return ('tipos_tela.cadastro', (), {'id': self.id})
   
    @staticmethod
    def get_config():
        return { 
           'titulo'   : _(u"Cadastro de Tipos de telas"),
           'app'      : "tipos_tela",
           'required' : "descricao",
           'fields' : [
                       ('id',        _(u'Cód.'),      True),
                       ('descricao', _(u'Descrição'), False),
            ],
        }
    
    @staticmethod
    def success_url(): 
        return "tipos_tela.listagem"

class Funcao(models.Model):
    nome      = models.CharField(max_length=50, unique=True, verbose_name=__(u"Nome"))
    descricao = models.TextField(verbose_name=__(u"Descrição"))
    
    class Meta:
        verbose_name        = _(u'Função')
        verbose_name_plural = _(u'Funções')
        ordering            = ['nome']

    def __unicode__(self):
        return self.descricao
    
    @models.permalink                                        
    def get_absolute_url(self):                              
       return ('funcao.cadastro', (), {'id': self.id})
   
    @staticmethod
    def get_config():
        return { 
           'titulo'   : _(u"Cadastro de Funções"),
           'app'      : "funcao",
           'required' : "descricao",
           'fields' : [
                       ('id',        _(u'Cód.'),     True),
                       ('nome',      _(u'Nome'),     False) 
                       #('descricao', _(u'Descrição'),False) 
            ],
        }
    
    @staticmethod
    def success_url(): 
        return "funcao.listagem"

class ModoPref(models.Model):
    descricao = models.CharField(max_length=50, unique=True, verbose_name=__(u"Descrição"))
    
    class Meta:
        verbose_name        = _(u'Modo Preferencial de Imagem')
        verbose_name_plural = _(u'Modos Preferenciais de Imagem')
        ordering            = ['descricao']

    def __unicode__(self):
        return self.descricao
    
    @models.permalink                                        
    def get_absolute_url(self):                              
       return ('modo_pref.cadastro', (), {'id': self.id})
   
    @staticmethod
    def get_config():
        return { 
           'titulo'   : _(u"Cadastro de Modo preferencial de imagem"),
           'app'      : "modo_pref",
           'required' : "descricao",
           'fields' : [
                       ('id',        _(u'Cód.'),     True),
                       ('descricao', _(u'Descrição'),False) 
            ],
        }
    
    @staticmethod
    def success_url(): 
        return "modo_pref.listagem"

class Item(models.Model):
    descricao = models.CharField(max_length=50, unique=True, verbose_name=__(u"Descrição"))
    
    class Meta:
        verbose_name        = _(u'Item Incluso')
        verbose_name_plural = _(u'Itens Inclusos')
        ordering            = ['descricao']

    def __unicode__(self):
        return self.descricao
    
    @models.permalink                                        
    def get_absolute_url(self):                              
       return ('item.cadastro', (), {'id': self.id})
   
    @staticmethod
    def get_config():
        return { 
           'titulo'   : _(u"Cadastro de Item incluso"),
           'app'      : "item",
           'required' : "descricao",
           'fields' : [
                       ('id',        _(u'Cód.'),     True),
                       ('descricao', _(u'Descrição'),False) 
            ],
        }
    
    @staticmethod
    def success_url(): 
        return "item.listagem"
    
class Entrada(models.Model):
    descricao = models.CharField(max_length=50, unique=True, verbose_name=__(u"Descrição"))
    
    class Meta:
        verbose_name        = _(u'Entrada')
        verbose_name_plural = _(u'Entradas')
        ordering            = ['descricao']

    def __unicode__(self):
        return self.descricao
    
    @models.permalink                                        
    def get_absolute_url(self):                              
       return ('entrada.cadastro', (), {'id': self.id})
   
    @staticmethod
    def get_config():
        return { 
           'titulo'   : _(u"Cadastro de Entradas"),
           'app'      : "entrada",
           'required' : "descricao",
           'fields' : [
                       ('id',        _(u'Cód.'),     True),
                       ('descricao', _(u'Descrição'),False) 
            ],
        }
    
    @staticmethod
    def success_url(): 
        return "entrada.listagem"


################################################################################
############################ - CADASTRO PRINCIPAL - ############################
################################################################################

'''
class Televisor(models.Model):
    descricao = models.CharField(max_length=50, unique=True, verbose_name=__(u"Descrição"))
    
    class Meta:
        verbose_name        = _(u'Televisor')
        verbose_name_plural = _(u'Televisores')
        ordering            = ['descricao']

    def __unicode__(self):
        return self.descricao
    
    @models.permalink                                        
    def get_absolute_url(self):                              
       return ('televisor.cadastro', (), {'id': self.id})
   
    @staticmethod
    def success_url(): 
        return "televisor.listagem"
'''    
   