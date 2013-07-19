#-*- coding: utf-8 -*-
from django import forms
from models import *


class TelevisorConexaoForm(forms.ModelForm):
    class Meta:
        model = TelevisorConexao