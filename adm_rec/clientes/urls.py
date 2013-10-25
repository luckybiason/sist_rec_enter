#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('clientes',            
                       
        ## - Cadastro cliente
        url(r'^cadastro/$', 'views.cadastro', name='clientes.cadastro'),
        
        ## - Login/Logout
        url(r'^login/$',  'views.login',  name='clientes.login'),
        url(r'^logout/$', 'views.logout', name='clientes.logout'),
            
)
