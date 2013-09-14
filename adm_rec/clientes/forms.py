#-*- coding: utf-8 -*-
from django import forms
from models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
      
class ClienteLoginForm(forms.Form):
    login = forms.CharField(required=True, widget=forms.TextInput(attrs={ 'autocomplete' : "false" }))
    senha = forms.CharField(max_length=32, widget=forms.PasswordInput) 