#! / usr / bin / env python 
# - * - coding: UTF-8 - * -
#Agenda Cultural Barcelona
import xml.etree.ElementTree as etree
from django.shortcuts import render
from .models import Activbcn
from bs4 import BeautifulSoup
import datetime 
import urllib.request
import sqlite3
import requests
from django.contrib.admin.views.decorators import staff_member_required

idevento=""


@staff_member_required

def Obtenerdatosbcn(request):
    
    
    url = 'http://w10.bcn.es/APPS/asiasiacache/peticioXmlAsia?id=103'
    req = urllib.request.Request(url)
    statusCode = req.status_code
    if statusCode == 200:
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        tree = etree.parse(resp) 
        try:
            Actualizar_bcn(tree)  
        except:
                pass
    else:
        print(statusCode)
        
        
        
    url = 'http://w10.bcn.es/APPS/asiasiacache/peticioXmlAsia?id=104'
    req = urllib.request.Request(url)
    statusCode = req.status_code
    if statusCode == 200:
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        tree = etree.parse(resp) 
        try:
            Actualizar_bcn(tree)  
        except:
                pass
    else:
         print(statusCode)

    url = 'http://w10.bcn.es/APPS/asiasiacache/peticioXmlAsia?id=105'
    req = urllib.request.Request(url)
    statusCode = req.status_code
    if statusCode == 200:
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        tree = etree.parse(resp) 
        try:
            Actualizar_bcn(tree)  
        except:
                pass
    else:
         print(statusCode)
    
    Activbcns=Activbcn.objects.all()   
    return render(request, 'TFM1app/Activ_listbcn.html', {'Activbcns' : Activbcns})


def Actualizar_bcn(tree):       
    entries_name = tree.findall('.//acte')
    #print(entries)
    dirFichero = 'TFM1/TFM1app/static/Actualizabcn.txt'
    fichero = open(dirFichero, 'a')
    for i,entrie in enumerate(entries_name):
        #print (i+1)
        idevento=entrie[0].text
        idevento= str(idevento)
        titulo=entrie[1].text
        titulo=str(titulo)
        titulo =titulo.replace('\x92','')
        titulo =titulo.replace('\x96','')
        titulo =titulo.replace('\x91',"'")
        fecha=entrie[3]
        fechaevento=fecha[0].text
        fechaevento=str(fechaevento)
        fechafin=fecha[2].text
        fechafin= str(fechafin)
        clasi = entrie[7]
        tipo=clasi[0].text
        tipo= str(tipo.encode("utf-8"))
        traduce= dict()
        traduce ={
                  "Alimentació, medicina, sexualitat i psicologia":"Cursos y talleres",
                  "Artesania":"Ferias muestras y mercadillos ocasionales",
                  "Audiovisual":"Cursos y talleres",
                  
                  "Balls de diables i correfocs":"Teatro circo y danza",
                  "Balls tradicionals":"Teatro circo y danza",
                  
                  "Campanyes":"Solidaridad y sensibilización",
                  "Cant, música, dansa i balls ":"Música",
                  "Ceràmica":"Cursos y talleres",
                  "Cercaviles":"Fiestas populares y fiestas señaladas",
                  "Cinema":"Cine circuito no comercial",
                  "Còmic":"Cultura general",
                  "Colònies i casals":"Colonias",
                  "Conferències":"Congresos conferencias y coloquios",
                  "Col.loquis":"Congresos conferencias y coloquios",
                  "Costura":"Cursos y talleres",
                  "Cultura general":"Cultura general",
                  "Cursos i tallers":"Cursos y talleres",
                  "Consells de barri":"Congresos conferencias y coloquios",
                  "Cuina i gastronomia ":"Cursos y talleres",
                  "Circ":"Fiestas populares y fiestas señaladas",
                                    
                  "Dansa":"Teatro circo y danza",
                  "Debats":"Congresos conferencias y coloquios",
                  "Decoració":"Cursos y talleres",
                  "Diades": "Fiestas populares y fiestas señaladas",
                 
                  "Educació":"Cursos y talleres",
                  "Estètica":"Cursos y talleres",
                  "Economia i empresa":"Cursos y talleres",
                  "Exposicions":"Exposiciones",
                  "Esports":"Deportes",
                  "Electrònica, techno i dance":"Música",
                 
                  "Focs d'artifici":"Fiestas populares y fiestas señaladas",
                  "Festes a discoteques":"Fiestas populares y fiestas señaladas",
                  "Festes de Santa Eulàlia":"Fiestas populares y fiestas señaladas",
                  "Festes majors":"Fiestas populares y fiestas señaladas",
                  "Fires, mostres i salons":"Ferias muestras y mercadillos ocasionales",
                  
                  "Gimcanes":"Fiestas populares y fiestas señaladas",
                  
                  "Horari atraccions il.luminacions, etc ": "Visitas recorridos y excursiones",
                  "Homenatges i ofrenes ":"Premios concursos y galas",
                  
                  "Idiomes": "Cursos y talleres",
                  "Informàtica, Internet":"Cursos y talleres",
                  
                  "Literatura":"Literatura: actividades",
                  
                  "Màgia":"Cursos y talleres",
                  "Medi Ambient":"Cursos y talleres",
                  "Mobilitat i transports":"Cursos y talleres",
                  "Menjars populars":"Fiestas populares y fiestas señaladas",
                  "Música":"Música",
                  "Nens i nenes, actes per a":"Niños y niñas: actividades",
                  
                  "Premis de fotografia":"Premios concursos y galas",
                  "Premis, lliurament de":"Premios concursos y galas",
                  "Pregons":"Fiestas populares y fiestas señaladas",
                  "Plenaris de districte":"Congresos conferencias y coloquios",
                  "Plenaris de l'Ajuntament":"Congresos conferencias y coloquios",
                  "Petits mercats ocasionals":"Ferias muestras y mercadillos ocasionales",
                  "Pop i rock":"Música",
                  "Populars, actes":"Fiestas populares y fiestas señaladas",
                 
                  "Inauguracions i Cloendes":"Exposiciones",
                  "Jardineria":"Cursos y talleres",
                  "Jazz i blues":"Música",
                  "Jocs":"Niños y niñas: actividades",
                  "Jornada de portes obertes i Cloendes":"Fiestas populares y fiestas señaladas",
                  "Jornada de portes obertes":"Fiestas populares y fiestas señaladas",
                  
                  "Humor":"Teatro circo y danza",
                  "Història":"Visitas recorridos y excursiones",
                  
                  
                  "Religiosos, actes":"Religiosos actos",
                  "Rutes":"Visitas recorridos y excursiones",
                  
                  "Seminaris":"Cursos y talleres",
                  "Sardanes":"Teatro circo y danza",
                  
                  "Teatre":"Teatro circo y danza",
                  "Titelles":"Teatro circo y danza",
                  "Trobades":"Fiestas populares y fiestas señaladas",
                  "Taules rodones i tertúlies":"Congresos conferencias y coloquios",
                  "Visites guiades ":"Visitas recorridos y excursiones",
                 
                  }

       

        if tipo in traduce:
            tipo= traduce.get(tipo)
            
        else:
            tipo = "Cultura general" 
        
        if not ('2016' in  fechaevento and '2016' in  fechafin):
            fechaevento='01/01/2016'
            fechafin= '31/12/2016' 
           
        if not('2016' in  fechafin):
            fechafin=fechaevento
           
    
       
   
        fechaevento=datetime.datetime.strptime(fechaevento, "%d/%m/%Y").strftime("%Y-%m-%d")
        fechafin=datetime.datetime.strptime(fechafin, "%d/%m/%Y").strftime("%Y-%m-%d")
        if not Activbcn.objects.filter(  idevento  = idevento ).exists():
                nuevaactividad= Activbcn(tipo=tipo,idevento=idevento,titulo=titulo,fechaevento=fechaevento,fechafin=fechafin)
                #nuevaactividad.save()
        fichero.write(tipo +',' + idevento + ',' + titulo + ',' + fechaevento + ',' + fechafin + ',' +  '\n' ) 
        
    fichero.close() 
    


   
    