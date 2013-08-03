#-*- coding: utf-8 -*-
from django.contrib.auth.models import User

def user_logado(request):
    if not request.session.get('_auth_user_id'):
        return {  }
    user_logado = User.objects.get(pk=request.session.get('_auth_user_id'))
    return { 
            'USER_NAME'      : user_logado.username,
            'USER_SUPER'     : "true" if user_logado.is_superuser else "",
            'USER_EMAIL'     : user_logado.email,
            'USER_LAST_LOGIN': user_logado.last_login,
     }