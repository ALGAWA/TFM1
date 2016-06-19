# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Activbcn
from bs4 import BeautifulSoup
import datetime 
import sqlite3
import requests

idevento=""




def Activ_listbcn(request):
    """
    #Parte para extraer tipos de actividades
    dirFichero = 'D:/Pruebas34/fich_tiposBCN.txt'
    fichero = open(dirFichero, 'w')
    #Make request
    direc='http://guia.barcelona.cat/es/llistat?tipuscerca=agenda&cerca='
    req = requests.get(direc)
    # Check get Status Code = 200 = Right, exists
    statusCode = req.status_code
    if statusCode == 200:
        # Passed the content HTML of the web to an object BeautifulSoup()
        html = BeautifulSoup(req.text.encode("utf-8"), "html.parser")
        # Get all div where activities entries are
        entradas = html.find_all('div',{'class':'caixa'})
        sd=str(entradas).split('<div class="caixa"><h3>Agenda</h3><ul><li>')
        sd=sd[1].split('<a href="')    
        del sd[0]
        # print(sd)
        # Travel for all entries for extract data
        for i,entrada in enumerate(sd):
            hrf= entrada.split('">')
            direc= hrf[0].replace('amp;','')
            hrf=hrf[1].split('(')
            tipo=hrf[0]
            hrf=hrf[1].split(')')
            num=hrf[0]
            fichero.write(direc +',')
            fichero.write(tipo +',')   
            fichero.write(num +'\n')
        
        
        # print(direc,tipo,num)
        #fichero.write(str(entrada.getText() + '\n'))
    
    else:
        #print "Status Code %d" %statusCode  de error
        print (statusCode)
    
    fichero.close()
   

    #PArte para extraer actividades

    dirFichero = 'D:/Pruebas34/fich_activsBCN.txt'
    fichero = open(dirFichero, 'a')


    cabecera= 'http://guia.barcelona.cat/es/llistat'
    cola1='?pg=search&cerca=*:*&tr=619&sort=proxdate,asc&af=code_prop&c=00619*&nr='
    #sd=direc.split('&nr=10')
    #cola2=sd[1]
    cola2='&code0=0061901004'
    tipo="Colonias"
    num='764'
    enlace=cabecera + cola1 + num + cola2
    #print(enlace)

    #Make request
    #req = requests.get(url)     &nr=441 (put number of registers found) 
    req = requests.get(enlace)

    # Check get Status Code = 200 = Right, exists
    statusCode = req.status_code
    if statusCode == 200:
        html = BeautifulSoup(req.text.encode("utf-8"), "html.parser")

        # Get all div where activities entries are
        entradas = html.find_all('div',{'class':'dades'})
        print("No he pasado el if")
        
            # Travel for all entries for extract data
        for i,entrada in enumerate(entradas):
            print (i+1)
           
            sd=str(entrada)
           
            if('Cuándo'in sd):
                sd=sd.split('</a></h3>')
                var=sd[0].split('.html">')
                tem=var[0].split('_')
                idevento=tem[1]
                titulo=var[1]
                print(idevento)
                print(titulo)
                var=sd[1]
                #print("esto es sd", sd)
                var=var.split('Cuándo:</dt><dd>')
                # sd=var[1].split('</dd><dt>Dirección')
                sd=var[1].split('</dd>')
                var=sd[0]
                #print(var)
        
                if(len(var)< 11):
                    fechaevento=sd[0]
                    fechaevento=fechaevento.rstrip( )
                    fechaevento= datetime.datetime.strptime(fechaevento, "%d/%m/%Y").strftime("%Y-%m-%d")
                    fechaevento=fechaevento.replace('/','-')
                    print(fechaevento)
                    fechafin=fechaevento
                    print(fechafin)
                    nuevaactividad= Activbcn(tipo=tipo,idevento=idevento,titulo=titulo,fechaevento=fechaevento,fechafin=fechafin)
                    nuevaactividad.save()
                    fichero.write(tipo +',' + idevento + ',' + titulo + ',' + fechaevento + ',' + fechafin + ',' +  '\n' )
            
                else:
                    if('2016' in  var):
                        var=var.split('al ')
                        fechafin=var[1]
                        fechafin=fechafin.rstrip(".")
                        fechafin= datetime.datetime.strptime(fechafin, "%d/%m/%Y").strftime("%Y-%m-%d")
                        fechafin=fechafin.replace('/','-')
                        print(fechafin)
                        sd=var[0]
                        sd=sd.split('Del ')
                        #print(sd)
                        fechaevento=sd[1]
                        fechaevento=fechaevento.rstrip( )
                        fechaevento= datetime.datetime.strptime(fechaevento, "%d/%m/%Y").strftime("%Y-%m-%d")
                        fechaevento= fechaevento.replace('/','-')
                        print(fechaevento)
                        nuevaactividad= Activbcn(tipo=tipo,idevento=idevento,titulo=titulo,fechaevento=fechaevento,fechafin=fechafin)
                        nuevaactividad.save()
                        fichero.write(tipo +',' + idevento + ',' + titulo + ',' + fechaevento + ',' + fechafin + ',' +  '\n' )
   
                    else:
                        fechaevento='2016-01-01'
                        fechafin='2016-12-31'
                        nuevaactividad= Activbcn(tipo=tipo,idevento=idevento,titulo=titulo,fechaevento=fechaevento,fechafin=fechafin)
                        nuevaactividad.save()
                        fichero.write(tipo +',' + idevento + ',' + titulo + ',' + fechaevento + ',' + fechafin + ',' +  '\n' )
   
        
            
            
       
    else:
        #print "Status Code %d" %statusCode  de error
        print (statusCode)
    
        
        
    fichero.close()
    """
    Activbcns=Activbcn.objects.all()   
    return render(request, 'TFM1app/Activ_listbcn.html', {'Activbcns' : Activbcns})
