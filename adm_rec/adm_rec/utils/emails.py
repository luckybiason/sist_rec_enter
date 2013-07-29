# -*- coding: utf-8 -*-
from django.core.mail import send_mail, send_mass_mail, EmailMessage
from django.conf      import settings

def envia_email(assunto, texto, destinatarios):
    msg = EmailMessage(assunto, texto, settings.EMAIL_HOST_USER, destinatarios)
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()