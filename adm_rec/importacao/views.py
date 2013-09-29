#-*- coding: utf-8 -*-
from django.shortcuts                 import redirect,render
from django.contrib.auth.decorators   import login_required
from adm_rec.utils.fileDownloadUpload import upload_file
from django.conf                      import settings
from methods                          import importar_televisores

@login_required
def televisores_importacao(request):
    titulo = "Importação de Televisores"
    
    if request.method == 'POST':
        arquivo = request.FILES.get("arquivo")
        if arquivo:
            arquivo_nome  = "importacao_televisores.csv"
            arquivo_url   = "%s/tmp/%s" % (settings.MEDIA_ROOT,arquivo_nome)
            file          = upload_file(request, 'arquivo')
            arquivo_error, arquivo_nome = importar_televisores(request, file, arquivo_url)# se arquivo_error for None, importou tudo.
            file.close()
            concluido = True
    
    return render(request, "importacao_televisores.html", locals())

