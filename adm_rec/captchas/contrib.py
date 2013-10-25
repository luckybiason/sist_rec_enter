#-*- coding: utf-8 -*-
from django.conf import settings

# Captchas disponiveis:
# 'motion', 'reorderCapt', 'ebword', 'pilcapt'

def client_captcha(request):
    try:
        captcha_path = settings.CAPTCHA_TYPE if settings.CAPTCHA_TYPE else 'motion'
    except:
        captcha_path = 'motion'
    return {
            'CAPTCHA_PATH_BODY' : captcha_path+'/captcha_body.html' ,
            'CAPTCHA_PATH_HEAD' : captcha_path+'/captcha_header.html' ,
    }