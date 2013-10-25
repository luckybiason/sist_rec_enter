#-*- coding: utf-8 -*-
from django.shortcuts                 import redirect,render
from django.contrib.auth.decorators   import login_required, user_passes_test
from adm_rec.utils.fileDownloadUpload import upload_file
from django.conf                      import settings
from methods                          import *

@login_required
def televisores_importacao(request):
    titulo = "Importação de Televisores"
    
    if request.method == 'POST':
        arquivo = request.FILES.get("arquivo")
        if arquivo:
            arquivo_nome    = "importacao_televisores.csv"
            arquivo_url     = "%s/tmp/%s" % (settings.MEDIA_ROOT,arquivo_nome)
            file            = upload_file(request, 'arquivo')
            status, retorno = importar_televisores(request, file, arquivo_url)
            if status:
                messages.success(request, 'Os televisores foram importadas com sucesso.')
                messages.success(request, 'Total importados: %s' % arquivo_nome)
            arquivo_nome = retorno
            file.close()
    else:
        status = True
    
    return render(request, "importacao_televisores.html", locals())

@login_required
def lojas_importacao(request):
    titulo = "Importação de Lojas"
    
    if request.method == 'POST':
        arquivo = request.FILES.get("arquivo")
        if arquivo:
            arquivo_nome  = "importacao_lojas.csv"
            arquivo_url     = "%s/tmp/%s" % (settings.MEDIA_ROOT,arquivo_nome)
            file            = upload_file(request, 'arquivo')
            status, retorno = importar_lojas(request, file, arquivo_url)
            if status:
                messages.success(request, 'As lojas foram importadas com sucesso.')
                messages.success(request, 'Total importados: %s' % arquivo_nome)
            arquivo_nome = retorno
            file.close()
    else:
        status = True
    
    return render(request, "importacao_lojas.html", locals())

@login_required
def tel_lojas_importacao(request):
    titulo = "Importação de Televisores para lojas"
    
    if request.method == 'POST':
        arquivo = request.FILES.get("arquivo")
        if arquivo:
            arquivo_nome  = "importacao_tel_lojas.csv"
            arquivo_url     = "%s/tmp/%s" % (settings.MEDIA_ROOT,arquivo_nome)
            file            = upload_file(request, 'arquivo')
            status, retorno = importar_tel_lojas(request, file, arquivo_url)
            if status:
                messages.success(request, 'As relações foram importadas com sucesso.')
                messages.success(request, 'Total importadas: %s' % arquivo_nome)
            arquivo_nome = retorno
            file.close()
    else:
        status = True
    
    return render(request, "importacao_tel_lojas.html", locals())

@login_required
@user_passes_test(lambda u: u.is_superuser)
def exportacao(request):
    titulo = "Exportação de Dados"
    
    if request.method == 'POST':
        tipo = request.POST.get("tipo","")
        if tipo:
            status, retorno, arquivo_erros = exportar_dados(request, tipo)
            
    return render(request, "exportacao.html", locals())    