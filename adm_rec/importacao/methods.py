# -*- coding: utf-8 -*-
import os
import csv
import commands
from django.contrib                   import messages
from django.core.files.base           import ContentFile
from django.core.files.storage        import default_storage
from adm_rec.utils.fileDownloadUpload import upload_file
from adm_rec.utils.strings            import del_acento
from televisores.models               import Televisor

csv_mime_type = ['text/comma-separated-values', 
                 'text/csv', 
                 'text/anytext',
                 'application/csv', 
                 'application/excel', 
                 'application/vnd.ms-excel', 
                 'application/vnd.msexcel',
                 ]

def importar_televisores(request, file, arquivo_url):
    '''
        Função Utilizada na Importação de Televisores.
        Le um arquivo .csv com os dados do televisor.
        Retorna True se importou, senão,
        retorna false e o caminho de um arquivo.csv contendo detalhes dos erros.
    '''
    tvs_nao_import_csv=[]
    
    def ler_csv(arq):
        if not arq.content_type in csv_mime_type:
            messages.error(request, "Esse não é um arquico csv válido. Entre com outro arquivo.")
            return None
        try:
            reader = csv.reader(arq, delimiter = '|')
            return [ linha for linha in reader]
        except IOError,msg:
            return None
    
    def gravar(linhas):
        try:
            with open(arquivo_url,'w+') as fi:
                out = csv.writer(fi, delimiter='|')
                out.writerows([("Cód. Televisor", "Erro")])
                out.writerows(linhas)
            return arquivo_url
        except IOError,msg:
             return None
    
    arquivo = ler_csv( file )
    if not arquivo:
        return False, "Esse não é um arquivo csv válido, entre com outro arquivo."
    
    qtd_televisores_salvos = 0
    indice_linha = 0
        
    for linha in arquivo:
        id = linha[0].replace("'","").strip()
            
        if Televisor.objects.filter(id=id).exists():
            televisor = Televisor.objects.get(id=id)
        else:
            televisor = Televisor()
            
        try:
            televisor.nome             = linha[1].replace("'","").strip()
            televisor.imagem           = linha[2].replace("'","").strip()
            televisor.marca_id         = linha[3].replace("'","").strip()
            televisor.polegadas        = linha[4].replace("'","").strip()
            televisor.altura           = linha[5].replace("'","").strip()
            televisor.largura          = linha[6].replace("'","").strip()
            televisor.profundidade     = linha[7].replace("'","").strip()
            televisor.peso             = linha[8].replace("'","").strip()
            televisor.potencia         = linha[9].replace("'","").strip()
            televisor.tipo_de_tela_id  = linha[10].replace("'","").strip()
            televisor.resolucao        = linha[11].replace("'","").strip()
            televisor.formato_tela     = linha[12].replace("'","").strip()
            televisor.consumo_energia  = linha[13].replace("'","").strip()
            televisor.is_full_hd       = linha[14].replace("'","").strip()
            televisor.is_smart_tv      = linha[15].replace("'","").strip()
            televisor.is_hdtv          = linha[16].replace("'","").strip()
            televisor.is_3d            = linha[17].replace("'","").strip()
            televisor.has_pip          = linha[18].replace("'","").strip()
            televisor.has_sap          = linha[19].replace("'","").strip()
            televisor.has_conversor    = linha[20].replace("'","").strip()
            televisor.alimentacao      = linha[21].replace("'","").strip()
            televisor.especificacao    = linha[22].replace("'","").strip()
            televisor.site             = linha[23].replace("'","").strip()
            televisor.video            = linha[24].replace("'","").strip()
            
            televisor.save()
        except Exception, ex:
           tvs_nao_import_csv.append( (id, ex) )
       
    if tvs_nao_import_csv:
        return False, gravar(tvs_nao_import_csv)
    else:
        messages.success(request, 'Os televisores foram importadas com sucesso.')
        messages.success(request, 'Total importados: %s' % str(qtd_televisores_salvos))
        return True, ""
