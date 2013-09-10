#-*- coding: utf-8 -*-
from django.db import models

USOS_INFO = {    
   "Jogos"     : [1],   
   "Blue-Ray"  : [2],
   "HDTV"      : [2],    
   "TV Aberta" : [3],
   "TV a cabo" : [3], 
   "DVD"       : [3],       
}

USOS_PESOS = { key : peso[0] for (key,peso) in  USOS_INFO.items() }

RESOLUCAO_PESOS ={
   'Normal'  : 3, 
   'HD'      : 2, 
   'Full HD' : 1,               
}

USOS_CHOICES = [
   ( "DVD",       "DVD" ),
   ( "Blue-Ray",  "Blue-Ray" ),
   ( "HDTV",      "HDTV" ),
   ( "TV Aberta", "TV Aberta" ),
   ( "TV a cabo", "TV a cabo" ),
   ( "Jogos",     "Jogos" ),
]

APARELHOS_INFO = {
 "Blu-ray"      : ["HDMI"], 
 "DVD"          : ["Conexão AV"],
 "Playstation"  : ["Conexão AV", "HDMI"], 
 "Xbox"         : ["Conexão AV", "HDMI"],
 "Wii U"        : ["HDMI"], 
 "PC/Notebook"  : ["RGB","HDMI"],
 "TV a cabo"    : ["Conexão AV"],
 "TV a cabo HD" : ["HDMI"],
}

APARELHOS_CHOICES = ( (key,key) for (key,info) in APARELHOS_INFO )
