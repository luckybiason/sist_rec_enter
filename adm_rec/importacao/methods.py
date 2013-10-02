# -*- coding: utf-8 -*-
import os
import csv
import commands
from django.conf                      import settings
from django.contrib                   import messages
from django.core.files.base           import ContentFile
from django.core.files.storage        import default_storage
from adm_rec.utils.fileDownloadUpload import upload_file
from adm_rec.utils.strings            import del_acento

## Modelo de dados
from televisores.models               import Televisor, TelevisorLoja
from lojas.models                     import Loja

csv_mime_type = ['text/comma-separated-values', 
                 'text/csv', 
                 'text/anytext',
                 'application/csv', 
                 'application/excel', 
                 'application/vnd.ms-excel', 
                 'application/vnd.msexcel',
                 ]

def importacao(request, file, arquivo_url, function_depara):
    '''
        Função Utilizada na Importação genérica.
        Le um arquivo .csv com os dados do objeto.
        Retorna True se importou, senão,
        retorna false e o caminho de um arquivo.csv contendo detalhes dos erros.
    '''
    nao_import_csv=[]
    
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
                out.writerows([("Cód.", "Erro")])
                out.writerows(linhas)
            return arquivo_url
        except IOError,msg:
             return None
    
    arquivo = ler_csv( file )
    if not arquivo:
        return False,''
    
    qtd_salvos = 0
    indice_linha = 0
        
    for linha in arquivo:
        try:
            function_depara(linha)
            qtd_salvos = qtd_salvos+1
        except Exception, ex:
           nao_import_csv.append( (linha[0], ex) )
           
    if nao_import_csv:
        return False, gravar(nao_import_csv)
    else:
        return True, str(qtd_salvos)

def importar_televisores(request, file, arquivo_url):
    
    def function_depara(linha):
        id = linha[0].replace("'","").strip()
        if Televisor.objects.filter(id=id).exists():
            televisor = Televisor.objects.get(id=id)
        else:
            televisor = Televisor()
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
    
    return importacao(request, file, arquivo_url, function_depara)

def importar_lojas(request, file, arquivo_url):
    
    def function_depara(linha):
        id = linha[0].replace("'","").strip()
        if Loja.objects.filter(id=id).exists():
            loja = Loja.objects.get(id=id)
        else:
            loja = Loja()
        
        loja.nome = linha[1].replace("'","").strip()
        loja.logo = linha[2].replace("'","").strip()
        loja.site = linha[3].replace("'","").strip()
        loja.save()
    
    return importacao(request, file, arquivo_url, function_depara)

def importar_tel_lojas(request, file, arquivo_url):
    
    def function_depara(linha):
        id = linha[0].replace("'","").strip()
        if TelevisorLoja.objects.filter(id=id).exists():
            tel_loja = TelevisorLoja.objects.get(id=id)
        else:
            tel_loja = TelevisorLoja()
            
        tel_loja.televisor_id = linha[1].replace("'","").strip()
        tel_loja.loja_id      = linha[2].replace("'","").strip()
        tel_loja.preco        = linha[3].replace("'","").strip()
        tel_loja.num_parcela  = linha[4].replace("'","").strip()
        tel_loja.val_parcela  = linha[5].replace("'","").strip()
        tel_loja.site         = linha[6].replace("'","").strip()
        tel_loja.obs          = linha[7].replace("'","").strip()
        tel_loja.save()
    
    return importacao(request, file, arquivo_url, function_depara)


def exportar_dados(request, tipo):
    
    def gravar(linhas, arquivo_url, header=None):
        n_import = []
        try:
            with open(arquivo_url,'w+') as fi:
                out = csv.writer(fi, delimiter='|')
                if header:
                    out.writerows(header)
                for linha in linhas:
                    try:
                        out.writerows([linha])
                    except Exception, ex:
                        n_import.append( (linha[0], ex) )
            return arquivo_url, n_import
        except Exception,msg:
             return None
    
    def export_depara_televisor():
        dados    = []
        for televisor in Televisor.objects.all():
                dados.append((
                  televisor.id,              
                  str(televisor.nome),
                  televisor.imagem,          televisor.marca_id,    televisor.polegadas,
                  televisor.altura,          televisor.largura,     televisor.profundidade,  televisor.peso,            televisor.potencia,
                  televisor.tipo_de_tela_id, televisor.resolucao,   televisor.formato_tela,  televisor.consumo_energia, televisor.is_full_hd,
                  televisor.is_smart_tv,     televisor.is_hdtv,     televisor.is_3d,         televisor.has_pip,         televisor.has_sap,
                  televisor.has_conversor,   televisor.alimentacao, 
                  str(televisor.especificacao), 
                  televisor.site, televisor.video,
                ))
        return dados
    
    def export_depara_loja():
        dados = []
        for loja in Loja.objects.all():
            dados.append( ( loja.id, loja.nome, loja.logo, loja.site ) )
        return dados
    
    def export_depara_tel_loja():
        dados    = []
        for tel_loja in TelevisorLoja.objects.all():
                dados.append((
                  tel_loja.id,
                  tel_loja.televisor_id,
                  tel_loja.loja_id,
                  tel_loja.preco,
                  tel_loja.num_parcela,
                  tel_loja.val_parcela,
                  tel_loja.site,
                  tel_loja.obs,
                ))
        return dados
    
    EXPORT = {
            'televisor' : [ 'exportacao_televisores.csv', export_depara_televisor],
            'lojas'     : [ 'exportacao_lojas.csv',       export_depara_loja],
            'tel_loja'  : [ 'exportacao_tel_lojas.csv',       export_depara_tel_loja],
    }
    
    tipo_exportar     = EXPORT[tipo]
    dados             = tipo_exportar[1]()
    arquivo_nome      = tipo_exportar[0]
    arquivo_url       = "%s/tmp/%s" % (settings.MEDIA_ROOT,arquivo_nome)
    status , n_import = gravar(dados, arquivo_url)
    
    if n_import:
        arquivo_url_erro = "%s/tmp/erros_%s" % (settings.MEDIA_ROOT,arquivo_nome)
        gravar(n_import, arquivo_url_erro ,[("Cód.", "Erro")])
        return bool(status), arquivo_nome, "erros_"+arquivo_nome
    
    return bool(status), arquivo_nome, ""