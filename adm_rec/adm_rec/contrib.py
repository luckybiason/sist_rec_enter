#-*- coding: utf-8 -*-
from django.contrib.auth.models import User

def user_logado(request):
    user_logado = User.objects.get(pk=request.session.get('_auth_user_id'))
    return { 
            'USER_NAME' : user_logado.first_name,
            'USER_SUPER': "true" if user_logado.is_superuser else "",
            'USER_ADM'  : "true" if user_logado.is_staff else "",
     }