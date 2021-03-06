#-*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.utils.translation import ugettext as _ , ugettext_lazy as __
from django.core.urlresolvers import reverse

################################################################################
########################### - CADASTROS AUXILIARES - ########################### 
################################################################################

class Marca(models.Model):
    descricao = models.CharField(max_length=50, unique=True, verbose_name=__(u"Descrição"))
    imagem    = models.ImageField(upload_to='img_marcas', blank=False, null=False, verbose_name=__(u"Logo:"))
    
    class Meta:
        verbose_name        = _(u'marca')
        verbose_name_plural = _(u'marcas')
        ordering            = ['descricao']

    def __unicode__(self):
        return self.descricao
    
    @models.permalink                                        
    def get_absolute_url(self):                   
       return ('marcas.cadastro', (), {'id': self.id})
   
    @staticmethod
    def get_config():
        return { 
           'titulo'   : _(u"Cadastro de Marcas"),
           'app'      : "marcas",
           'required' : "descricao",
           'fields' : [
                       ('id',        _(u'Cód.'),      True),
                       ('descricao', _(u'Descrição'), False),
            ],
        }
    
    @staticmethod
    def success_url(): 
        return "marcas.listagem"

class TipoTela(models.Model):
    descricao     = models.CharField(max_length=50, unique=True, verbose_name=__(u"Descrição"))
    imagem        = models.FileField(upload_to='img_telas', blank=False, null=False, verbose_name=__(u"Imagem ilustrativa:"))
    especificacao = models.TextField(verbose_name=__(u"Texto explicativo"))
    
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
           'required' : "nome",
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

TIPO_ALIMENTACAO   = [
 ('1','110v'), ('2','220v'), ('b','Bivolt')
]

RESOLUCOES_CHOICES = [
 ('Normal','Normal'), ('HD','HD'), ('Full HD','Full HD')
]

class Televisor(models.Model):
    ## Dados Básicos
    nome    = models.CharField(max_length=50,  unique=True, verbose_name=__(u"Nome:"))
    imagem  = models.ImageField(upload_to='img_televisores', blank=False, null=False, verbose_name=__(u"Foto:"))
    marca   = models.ForeignKey(Marca,       blank=False, null=False, verbose_name=__(u"Marca:"))
    funcoes = models.ManyToManyField(Funcao, blank=True,  null=True,  verbose_name=__(u"Funções:"), related_name='televisores')
    ## Medidas
    polegadas       = models.FloatField(verbose_name=__(u"Polegadas:"))
    altura          = models.FloatField(verbose_name=__(u"Altura:"))
    largura         = models.FloatField(verbose_name=__(u"Largura:"))
    profundidade    = models.FloatField(verbose_name=__(u"Profundidade:"), blank=True, null=True)
    peso            = models.FloatField(verbose_name=__(u"Peso:"),         blank=True, null=True)
    potencia        = models.FloatField(verbose_name=__(u"Potência:"),     blank=True, null=True)
    ## Tela
    tipo_de_tela    = models.ForeignKey(TipoTela, blank=False, null=False, verbose_name=__(u"Tipo de tela:"))
    resolucao       = models.CharField(max_length=150, verbose_name=__(u"Resolução"), blank=False, null=False, choices=RESOLUCOES_CHOICES)
    formato_tela    = models.CharField(max_length=150, verbose_name=__(u"Formato da tela:"), blank=True, null=True)
    consumo_energia = models.FloatField(verbose_name=__(u"Consumo Energ.:"), blank=True, null=True)
    ## Flags
    is_full_hd    = models.BooleanField( verbose_name=__(u"Full HD"),  blank=True)
    is_smart_tv   = models.BooleanField( verbose_name=__(u"Smart TV"), blank=True)
    is_hdtv       = models.BooleanField( verbose_name=__(u"HDTV"),     blank=True)
    is_3d         = models.BooleanField( verbose_name=__(u"3D"),       blank=True)
    has_pip       = models.BooleanField( verbose_name=__(u"PIP"),      blank=True)
    has_sap       = models.BooleanField( verbose_name=__(u"SAP"),      blank=True)
    has_conversor = models.BooleanField( verbose_name=__(u"Conversor Digital"), blank=True) 
    ## Outros
    alimentacao   = models.CharField(max_length=150, verbose_name=__(u"Alimentação"), choices=TIPO_ALIMENTACAO, blank=True, null=True)
    especificacao = models.TextField(verbose_name=__(u"Outras especificações"), blank=True, null=True)
    site          = models.CharField(max_length=150, verbose_name=__(u"Site"),  blank=True, null=True)
    video         = models.CharField(max_length=150, verbose_name=__(u"Link de Video"), blank=True, null=True)
    
    ## Estatisticas 
    visitado    = models.IntegerField(verbose_name=__(u"Visitado:"),    blank=True, null=True)
    recomendado = models.IntegerField(verbose_name=__(u"Recomendado:"), blank=True, null=True)
    data_cadastro = models.DateField(default=datetime.now)
    
    class Meta:
        verbose_name        = _(u'Televisor')
        verbose_name_plural = _(u'Televisores')
        ordering            = ['nome']
        db_table            = 'televisores'

    def __unicode__(self):
        return self.nome
    
    def get_nota_media(self):
        from portal.models import Comentario
        notas = Comentario.objects.only("nota").filter(televisor=self)
        return reduce(lambda x,y: x+y, notas)/notas.count()
    
    def ja_comentado(self, cliente):
        from portal.models import Comentario
        return Comentario.objects.filter(cliente=cliente, televisor=self).exists()
    
    def ja_visitado(self, cliente):
        from portal.models import Visitado
        return Visitado.objects.filter(cliente=cliente, televisor=self).exists()
    
    def get_imagem(self): 
        return u'''<img src='/media/%s' height='40px'>''' % str(self.imagem)
    
    @models.permalink                                        
    def get_absolute_url(self):                              
       return ('televisor.cadastro', (), {'id': self.id})
   
    @staticmethod
    def success_url(): 
        return "televisor.listagem"
    
    @staticmethod
    def get_config():
        return { 
           'titulo'   : _(u"Cadastro de Televisores"),
           'app'      : "televisor",
           'required' : "nome polegadas altura largura marca tipo_de_tela",
           'fields' : [
                       #('get_imagem', _(u'Imagem'), True),
                       ('id',   _(u'Cód.'), False),
                       ('nome', _(u'Nome'), False),
            ],
        }
        
    def lojas(self):
        return [ tel_loja.loja for tel_loja in TelevisorLoja.objects.filter(televisor=self)]
    
    def adicionar_visita(self, cliente=None):
        from portal.models import Visitado
        if cliente:
             Visitado.objects.create(cliente=cliente, televisor=self)
        self.visitado = self.visitado + 1
        self.save()
   

class TelevisorConexao(models.Model):    
    televisor = models.ForeignKey(Televisor, blank=False, null=False)
    conexao   = models.ForeignKey(Entrada,   blank=False, null=False, verbose_name=__(u"Conexão:"))
    qntd      = models.FloatField(default=1, verbose_name=__(u"Quantidade:"))
    obs       = models.TextField(verbose_name=__(u"Observações:"))
    
    def __unicode__(self):
        return self.conexao.descricao
    
    class Meta:
        ordering = ['conexao']
        unique_together = [('televisor','conexao')]
        
    @staticmethod
    def success_url(): 
        return "conexoes.listagem"

class TelevisorItens(models.Model):    
    televisor = models.ForeignKey(Televisor, blank=False, null=False)
    item      = models.ForeignKey(Item,      blank=False, null=False, verbose_name=__(u"Item:"))
    qntd      = models.FloatField(default=0, verbose_name=__(u"Quantidade:"))
    obs       = models.TextField(verbose_name=__(u"Observações:"))
    
    class Meta:
        ordering = ['item']
        unique_together = [('televisor','item')]

from lojas.models import Loja
class TelevisorLoja(models.Model):    
    televisor   = models.ForeignKey(Televisor, verbose_name=__(u"Televisor:"))
    loja        = models.ForeignKey(Loja,      verbose_name=__(u"Loja:"))
    preco       = models.FloatField(default=0, verbose_name=__(u"Preço:"))
    num_parcela = models.FloatField(default=0, verbose_name=__(u"Quantidade de parcelas:"))
    val_parcela = models.FloatField(default=0, verbose_name=__(u"Valor de parcelas:"))
    site        = models.CharField(max_length=150, verbose_name=__(u"Página:"))
    obs         = models.TextField(verbose_name=__(u"Observações:"))
    
    class Meta:
        ordering = ['loja']
        unique_together = [('televisor','loja')]


   