#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('importacao',            
    # Importação de dados               
    url(r'^televisores/$', 'views.televisores_importacao', name='importacao.televisores'),
    url(r'^lojas/$',       'views.lojas_importacao',       name='importacao.lojas'),
    url(r'^tel_lojas/$',   'views.tel_lojas_importacao',   name='importacao.tel_lojas'),
    # Exportação de dados                                    
    url(r'^exportacao/$',  'views.exportacao',             name='importacao.exportacao'),
        
)
