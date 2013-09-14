#-*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _ , ugettext_lazy as __
from django.core.urlresolvers import reverse
from portal.models import Comentario

################################################################################
############################ - CADASTRO PRINCIPAL - ############################
################################################################################

class Cliente(models.Model):
    ## - Dados Básicos (cadastro)
    nome    = models.CharField(max_length=50,  verbose_name=__(u"Nome:"))
    email   = models.CharField(max_length=60,  verbose_name=__(u"Email:"), unique=True)
    senha   = models.CharField(max_length=15,  verbose_name=__(u"Senha:"))
    
    ## - Perfil Filtragem (armazena os filtros do usuario)
    distancias = models.IntegerField()            # Distância
    usos       = models.CharField(max_length=200) # Códigos dos Usos
    tip_telas  = models.CharField(max_length=200) # Códigos dos Tipos de Tela
    preco_min  = models.FloatField(default=0)     # Preço Minimo
    preco_max  = models.FloatField(default=0)     # Preço Máximo
    
    class Meta:
        verbose_name        = _(u'cliente')
        verbose_name_plural = _(u'clientes')
        ordering            = ['nome','email']

    def __unicode__(self):
        return self.nome
    
class ClienteComentarios(models.Model):
    comentario = models.ForeignKey(Comentario, blank=False, null=False)
    cliente    = models.ForeignKey(Cliente,    blank=False, null=False)
    
    class Meta:
        ordering = ['cliente','comentario']

    def __unicode__(self):
        return self.comentario
    
    