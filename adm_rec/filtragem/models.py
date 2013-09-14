#-*- coding: utf-8 -*-
from django.db import models

USOS_INFO = {    
   "Jogos"     : [2],   
   "Blue-Ray"  : [1],
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
   ( "DVD",       "DVD",       "img/dvd_icon.png"),
   ( "Blue-Ray",  "Blue-Ray",  "img/blu-ray_icon.png"),
   ( "HDTV",      "HDTV",      "img/HD_icon.png"),
   ( "TV Aberta", "TV Aberta", "img/tva_con.png" ),
   ( "TV a cabo", "TV a cabo", "img/tvc_icon.png" ),
   ( "Jogos",     "Jogos",     "img/jogos2_icon.png" ),
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

APARELHOS_CHOICES = ( (key,key) for (key,info) in APARELHOS_INFO.items() )
