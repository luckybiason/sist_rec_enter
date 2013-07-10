#-*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django                     import forms
from datetime                   import date

class FormUser(forms.ModelForm):
    
    last_login  = forms.DateField(label =u'Último login:',     initial=date.today())
    date_joined = forms.DateField(label =u'Data de registro:', initial=date.today())
        
    def clean(self):
        print self.cleaned_data
        self.cleaned_data['last_login']  = '/'.join( str(date.today()).split('-')[::-1] )
        self.cleaned_data['date_joined'] = '/'.join( str(date.today()).split('-')[::-1] )
        print self.cleaned_data
        return self.cleaned_data
    
    class Meta:
        model = User
    
