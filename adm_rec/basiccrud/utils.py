#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import *
from django.conf import settings
from django.shortcuts import render_to_response

# - Icone para remover um registro
def get_delete_icon(id_obj,model):
    context = {
        'url': reverse(model.get_config()["app"]+".excluir", kwargs={'pk': id_obj}),
        'STATIC_URL': settings.STATIC_URL
    }
    return render_to_response("basic/_img_excl.html", context).content
    
# - Icone que mostra um ok ou não ok para campos booleanos
def get_boolean_icon(boole):
    context = {
        'bool': boole,
        'STATIC_URL': settings.STATIC_URL
    }
    return render_to_response("basic/_img_bool.html", context).content


#- Verifica se o objeto tem registros relacionados
def has_related_objects(model,obj):
    #return True
    if model._meta.get_all_related_objects():            
        for related_object in model._meta.get_all_related_objects():
            related = related_object.model.objects
            campo   = related_object.field.get_attname().replace('_id','')
            if related.get_query_set().filter(**{campo.lower():obj.id}):
                return True
    return False