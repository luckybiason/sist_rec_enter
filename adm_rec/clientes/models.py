#-*- coding: utf-8 -*-
from datetime import datetime
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
    usos       = models.CharField(max_length=200) # Códigos dos Usos
    aparelhos  = models.CharField(max_length=200) # Códigos dos Aparelhos
    preco_min  = models.FloatField(default=0)     # Preço Minimo
    preco_max  = models.FloatField(default=0)     # Preço Máximo
    tip_telas  = models.CharField(max_length=200) # Códigos dos Tipos de Tela
    tam_telas  = models.CharField(max_length=200) # Números dos Tamanhos de Tela
    distancia  = models.IntegerField()            # Distância
    
    ## - dt_cadastro
    data_cadastro = models.DateField(default=datetime.now)
    
    class Meta:
        verbose_name        = _(u'cliente')
        verbose_name_plural = _(u'clientes')
        ordering            = ['nome','email']

    def __unicode__(self):
        return self.nome
    
    def has_perfil(self):
        return any(self.usos, self.aparelhos, self.preco_min, self.preco_max, self.tip_telas, self.tam_telas, self.distancia)
    
class ClienteComentarios(models.Model):
    comentario = models.ForeignKey(Comentario, blank=False, null=False)
    cliente    = models.ForeignKey(Cliente,    blank=False, null=False)
    
    class Meta:
        ordering = ['cliente','comentario']

    def __unicode__(self):
        return self.comentario
    
    