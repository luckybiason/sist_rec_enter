# -*- coding: utf-8 -*-
from django.conf     import settings
from django.template.defaultfilters import slugify
from datetime        import datetime
from suds.client     import Client, WebFault
from suds.xsd.doctor import ImportDoctor, Import

def get_web_service():
    """
        Documentação dos métodos disponíveis:
            http://academico.engsupport.eti.br/servicos/cidades.asmx
    """
    imp = Import('http://www.w3.org/2001/XMLSchema')
    imp.filter.add('http://tempuri.org/')
    doctor = ImportDoctor(imp)
    client = Client('http://academico.engsupport.eti.br/servicos/cidades.asmx?WSDL', doctor=doctor)
    return client.service
    #from app_endereco.methods import * busca_cidades('SP')

def busca_cidades(estado):
    """
         Retorno do webservice:
         (CIDADES){
                _id = "CIDADES1"
                _rowOrder = "0"
                CODCID = "56"
                NOMCID = "ADOLFO"
                ESTCID = "SP"
                DDDCID = "17"
                CEPCID = "15230000"
            }
    """
    if not estado:
        return []
    else:
        try:
            cidades = get_web_service().RETORNA_CIDADES_ESTADO(estado)
            cidades = cidades.diffgram.NewDataSet.CIDADES
            return [ ( cid.CODCID,cid.NOMCID.capitalize()) for cid in cidades ]
        except WebFault, ex:
            return []

def busca_cidade_cod(cod_cidade):
    """
         Retorno do webservice:
         (CIDADES){
                _id = "CIDADES1"
                _rowOrder = "0"
                CODCID = "56"
                NOMCID = "ADOLFO"
                ESTCID = "SP"
                DDDCID = "17"
                CEPCID = "15230000"
            }
    """
    if not cod_cidade:
        return False
    else:
        try:
            cidade = get_web_service().RETORNA_CIDADE_ESPECIFICA(cod_cidade)
            cidade = cidade.diffgram.NewDataSet.CIDADES
            return cidade.NOMCID.capitalize()
        except WebFault, ex:
            pass
    return True  

def busca_estados():
    """
         Retorno do webservice:
         (ESTADOS){
            _id = "ESTADOS27"
            _rowOrder = "26"
            ESTCID = "TO"
         },
    """
    try:
        estados = get_web_service().RETORNA_ESTADOS()
        estados = estados.diffgram.NewDataSet.ESTADOS
        return [ ( cid._rowOrder, cid.ESTCID ) for est in estados ]
    except WebFault, ex:
        pass
    return True
      
def busca_estado(cod_estado):
    """
         Retorno do webservice: string com a sigla 
    """
    if not cod_estado:
        return False
    try:
        estado = get_web_service().RETORNA_ESTADO_ESPECIFICO(cod_estado)
        estado = estados.diffgram.NewDataSet.ESTADOS
        return [ ( cid._rowOrder, cid.ESTCID ) for est in estados ]
    except WebFault, ex:
        pass
    return True
    
def busca_cidade_por_cep(cep):
    """
         Retorno do webservice:
         (CIDADES){
                     _id = "CIDADES1"
                     _rowOrder = "0"
                     NOMCID = "SANTO ANDRE"
                     ESTCID = "SP"
                     CPICID = "9010000"
                     CPFCID = "9291280"
                     IBGEST = "25"
                     IBGCID = "2513851"
            }
    """
    if not cep:
        return False
    else:
        try:
            cidade = get_web_service().RETORNA_CIDADE_CEP(cep)
            cidade = cidade.diffgram.NewDataSet.CIDADES
            return cidade
        except WebFault, ex:
            pass
    return True  