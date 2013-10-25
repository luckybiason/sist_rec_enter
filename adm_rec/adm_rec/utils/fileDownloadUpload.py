#-*- coding: utf-8 -*-
import os
from django.http           import HttpResponse, HttpRequest
from adm_rec.utils.strings import del_acento


def getBytesFromFile(request_or_files, nome_input_file):
    assert isinstance(request_or_files, (dict, HttpRequest))
    
    if isinstance(request_or_files, HttpRequest): # request
        arquivoEnviado = request_or_files.FILES.get(nome_input_file, None)
    elif isinstance(request_or_files, dict): # files
        arquivoEnviado = request_or_files.get(nome_input_file, None)
        
    if not arquivoEnviado:
        raise('Nenhum arquivo enviado.')

    arquivoEnviado.seek(0)
    bytes = arquivoEnviado.read().encode('base64')
    arquivoEnviado.seek(0)
    return bytes

def downloadFileFromBytes(bytes, nome_arquivo, mime_type=None, salvar_em=None):
    '''
        Se 'salvar_em' for None, retorna um HttpResponse para o download do arquivo.
        Senão, salva o arquivo no diretório especificado.
    '''

    from mimetypes import guess_type
    mime_type = mime_type or guess_type(nome_arquivo)[0]
    bytes_arquivo = str(bytes).decode('base64')
    
    if salvar_em == None:
        resposta = HttpResponse(bytes_arquivo, mimetype=mime_type)
    
        resposta['Cache-Control'] = 'public'
        resposta['Content-Description'] = 'File Transfer'
        resposta['Content-Disposition'] = 'attachment; filename="%s"' \
            % (del_acento(nome_arquivo).encode('utf-8') if nome_arquivo else 'arquivo')
        resposta['Content-Transfer-Encoding'] = 'binary'
        return resposta
    else:
        os.chdir(salvar_em)
        arquivo = file(del_acento(nome_arquivo).encode('utf-8') if nome_arquivo else 'arquivo', 'w+')
        arquivo.write(bytes_arquivo)
        arquivo.close()
        
def upload_file(file, file_name):
    ''' Essa função recebe um arquivo ou um request para realizar o upload.
        file: pode receber o request ou um arquivo;
        file_name : recebe o nome do arquivo
        Retorna o arquivo'''
    assert isinstance(file, (dict, HttpRequest))

    if isinstance(file, HttpRequest): # request
        arquivo = file.FILES.get(file_name, None)
    elif isinstance(file, dict): # files
        arquivo = file.get(file_name, None)
    return arquivo
