#-*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
import datetime 

def size_validator(tamanho):
    if not int(tamanho)<=0:
        raise ValidationError("Medida inválida. Não pode ser negativa ou igual a zero.")
