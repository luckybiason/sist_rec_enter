#-*- coding: utf-8 -*-
from django  import forms
from models import ComponenteVisual

class FormCompVisual(forms.ModelForm):
    is_televisor = forms.BooleanField( widget=forms.HiddenInput() )
    class Meta:
        model = ComponenteVisual
