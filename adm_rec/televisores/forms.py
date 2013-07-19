#-*- coding: utf-8 -*-
from django import forms
from models import *

class TelevisorConexaoForm(forms.ModelForm):
    class Meta:
        model = TelevisorConexao
        
class TelevisorItensForm(forms.ModelForm):
    class Meta:
        model = TelevisorItens
            
class TelevisorLojaForm(forms.ModelForm):
    class Meta:
        model = TelevisorLoja