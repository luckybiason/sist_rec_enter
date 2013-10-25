#-*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django                     import forms
from datetime                   import date

class FormUser(forms.ModelForm):
    
    last_login  = forms.DateField(label =u'Último login:',     initial=date.today())
    date_joined = forms.DateField(label =u'Data de registro:', initial=date.today())
    
    class Meta:
        model = User
    
