#-*- coding: utf-8 -*-
from django.db                import models
from django.utils.translation import ugettext as _ , ugettext_lazy as __
from televisores.models       import Televisor

class Comentario(models.Model):
    televisor  = models.ForeignKey(Televisor, blank=False, null=False)
    nome       = models.CharField(max_length=50, verbose_name=__(u"Nome"))
    comentario = models.TextField(verbose_name=__(u"Comentário"))
    nota       = models.IntegerField(verbose_name=__(u"Nota"))
    data       = models.DateField(verbose_name=__(u"Nota"), auto_now=True)
    
    class Meta:
        verbose_name        = _(u'comentario')
        verbose_name_plural = _(u'comentarios')
        ordering            = ['data','-id']

    def __unicode__(self):
        return self.comentario
