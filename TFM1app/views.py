from django.shortcuts import render
from .models import Activmad
from bs4 import BeautifulSoup
import xml.etree.ElementTree as etree
import datetime 
import sqlite3
import requests
from TFM1app.viewbcn import idevento




req = requests.get('http://www.madrid.es/portales/munimadrid/es/Inicio/Cultura-ocio-y-deporte/Actividades-y-eventos?vgnextfmt=default&vgnextchannel=6381f073808fe410VgnVCM2000000c205a0aRCRD&vgnextoid=6381f073808fe410VgnVCM2000000c205a0aRCRD#')


def Activ_listmad(request):
    tipo=""
    titulo=""
    fechaevento='2016-03-05'
    fechafin='2016-03-05'
    descripcion=""
    idant=""
    idevento=""
    
    tree = etree.parse('D:\Pruebas34\Madridagenda100.xml')              
    root = tree.getroot()
#print(root.tag)
#print(root.attrib)
    for atributo in root.iter('atributo'):
        if (atributo.get('nombre')=='TIPO'):
            tipo = atributo.text[23:]
        if (atributo.get('nombre')=='ID-EVENTO'):
            idevento = atributo.text   
        if (atributo.get('nombre')=='TITULO'):
            titulo = atributo.text
        if (atributo.get ('nombre')=='FECHA-EVENTO'):
            fechaevento= atributo.text[0:10]
        if (atributo.get ('nombre')=='FECHA-FIN-EVENTO'):
            fechafin= atributo.text[0:10]
        if (atributo.get('nombre')=='DESCRIPCION'):
            descripcion = atributo.text 
        if (idant!=idevento):
            #print(tipo,idevento,titulo,fechaevento,fechafin,descripcion) 
            idant=idevento 
            nuevaactividad= Activmad(tipo=tipo,idevento=idevento,titulo=titulo,fechaevento=fechaevento,fechafin=fechafin,descripcion=descripcion)
            #nuevaactividad.save()
    Activmads=Activmad.objects.all()   
    return render(request, 'TFM1app/Activ_listMad.html', {'Activmads': Activmads})