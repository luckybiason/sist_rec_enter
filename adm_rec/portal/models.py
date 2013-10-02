#-*- coding: utf-8 -*-
from django.db                import models
from django.utils.translation import ugettext as _ , ugettext_lazy as __
from televisores.models       import Televisor
#from clientes.models          import Cliente

class Comentario(models.Model):
    televisor  = models.ForeignKey(Televisor, blank=False, null=False, related_name="televisor_comentado")
    nome       = models.CharField(max_length=50, verbose_name=__(u"Nome"))
    comentario = models.TextField(verbose_name=__(u"Comentário"))
    nota       = models.IntegerField(verbose_name=__(u"Nota"))
    data       = models.DateField(verbose_name=__(u"Data cadastro"), auto_now=True)
    cliente    = models.ForeignKey("clientes.Cliente", blank=True, null=True, related_name="dono_comentario")
    
    @staticmethod
    def get_cliente_comentarios(cliente): 
        return Comentario.objects.filter(cliente=cliente)
    
    @staticmethod
    def get_televisor_comentarios(televisor): 
        return Comentario.objects.filter(televisor=televisor)
    
    class Meta:
        verbose_name        = _(u'comentario')
        verbose_name_plural = _(u'comentarios')
        ordering            = ['data','-id']

    def __unicode__(self):
        return self.comentario

class Visitado(models.Model):
    televisor  = models.ForeignKey(Televisor,          blank=False, null=False, related_name="televisor_visitado")
    cliente    = models.ForeignKey("clientes.Cliente", blank=False, null=False, related_name="visitante")
    
    class Meta:
        db_table            = 'visitado'
        verbose_name        = _(u'visitado')
        verbose_name_plural = _(u'visitados')