#!/usr/bin/python
# -*- coding: utf-8 -*-
#XML Madrid

import urllib.request
from django.shortcuts import render
from .models import Activmad
from bs4 import BeautifulSoup
import xml.etree.ElementTree as etree
import datetime 
import sqlite3
import requests
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def Crear_mad(request):
    url = 'http://datos.madrid.es/egob/catalogo/206974-0-agenda-eventos-culturales-100.xml'
    req = requests.get(url)
    # Check get Status Code = 200 = Right, exists
    statusCode = req.status_code
    if statusCode == 200:
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        tree = etree.parse(resp)            
        root = tree.getroot()
        try:
            Obtenerdatosmad(root)
        except:
            pass
    else:
        print (statusCode)
        
    Activmads=Activmad.objects.all()   
    return render(request, 'TFM1app/Activ_listMad.html', {'Activmads': Activmads})

def Obtenerdatosmad(root):
    tipo=""
    titulo=""
    fechaevento='2016-03-05'
    fechafin='2016-03-05'
    descripcion=""
    idant=""
    idevento=""
    
    for atributo in root.iter('atributo'):
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
        if (atributo.get('nombre')=='TIPO'):
            tipo = atributo.text[23:]
        if (idant!=idevento):
            #print(tipo.encode("utf-8"),idevento,titulo.encode("utf-8"),fechaevento,fechafin,descripcion.encode("utf-8")) 
            idant=idevento 
            nuevaactividad= Activmad(tipo=tipo,idevento=idevento,titulo=titulo,fechaevento=fechaevento,fechafin=fechafin,descripcion=descripcion)
            #nuevaactividad.save()
    