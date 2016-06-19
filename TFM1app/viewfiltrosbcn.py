
from django.shortcuts import render
from .models import Activbcn
from bs4 import BeautifulSoup
import xml.etree.ElementTree as etree
import datetime 
import sqlite3
import requests




def Por_tipo_cinebarcelona(request):
    Cinesbcn = Activbcn.objects.raw('SELECT * FROM TFM1app_Activbcn WHERE  tipo  like "Cine%" ')
    return render(request, 'TFM1app/Cine_barcelona.html', {'Cinesbcn': Cinesbcn})

def Por_tipo_Colonias(request):
    Colonias = Activbcn.objects.raw('SELECT * FROM TFM1app_Activbcn WHERE  tipo  like "Colonias%" ')
    return render(request, 'TFM1app/Colonias_barcelona.html', {'Colonias': Colonias})


def Por_tipo_Congresos(request):
    Congresos = Activbcn.objects.raw('SELECT * FROM TFM1app_Activbcn WHERE  tipo  like "Congresos%" ')
    return render(request, 'TFM1app/Congresos_barcelona.html', {'Congresos': Congresos})

def Por_tipo_Deportes(request):
    Deportes = Activbcn.objects.raw('SELECT * FROM TFM1app_Activbcn WHERE  tipo  like "Deportes%" ')
    return render(request, 'TFM1app/Deportes_barcelona.html', {'Deportes': Deportes})

def Por_tipo_Exposiciones(request):
    Exposiciones = Activbcn.objects.raw('SELECT * FROM TFM1app_Activbcn WHERE  tipo  like "Exposiciones%" ')
    return render(request, 'TFM1app/Exposiciones_barcelona.html', {'Exposiciones': Exposiciones})

def Por_tipo_Ferias(request):
    Ferias = Activbcn.objects.raw('SELECT * FROM TFM1app_Activbcn WHERE  tipo  like "Ferias%" ')
    return render(request, 'TFM1app/Ferias_barcelona.html', {'Ferias': Ferias})

def Por_tipo_Fiestas(request):
    Fiestas = Activbcn.objects.raw('SELECT * FROM TFM1app_Activbcn WHERE  tipo  like "Fiestas%" ')
    return render(request, 'TFM1app/Fiestas_Barcelona.html', {'Fiestas': Fiestas})

def Por_tipo_Juegos(request):
    Juegos = Activbcn.objects.raw('SELECT * FROM TFM1app_Activbcn WHERE  tipo  like "Juegos%" ')
    return render(request, 'TFM1app/Juegos_barcelona.html', {'Juegos': Juegos})

def Por_tipo_Literatura(request):
    Conferencias = Activbcn.objects.raw('SELECT * FROM TFM1app_Activbcn WHERE  tipo  like "Literatura%" ')
    return render(request, 'TFM1app/Literatura_barcelona.html', {'Conferencias': Conferencias})


def Por_tipo_Moda(request):
    Modas = Activbcn.objects.raw('SELECT * FROM TFM1app_Activbcn WHERE  tipo  like "Moda%" ')
    return render(request, 'TFM1app/Moda_barcelona.html', {'Modas': Modas})

def Por_tipo_Musica(request):
    Musicas = Activbcn.objects.raw('SELECT * FROM TFM1app_Activbcn WHERE  tipo  like "M%sica%" ')
    return render(request, 'TFM1app/Musica_barcelona.html', {'Musicas': Musicas})

def Por_tipo_Ninos(request):
    Ninos = Activbcn.objects.raw('SELECT * FROM TFM1app_Activbcn WHERE  tipo  like "Ni%" ')
    return render(request, 'TFM1app/Ninos_barcelona.html', {'Ninos': Ninos})

def Por_tipo_Politicos(request):
    Politicos = Activbcn.objects.raw('SELECT * FROM TFM1app_Activbcn WHERE  tipo  like "Politicos%" ')
    return render(request, 'TFM1app/Politicos_barcelona.html', {'Politicos': Politicos})


def Por_tipo_Premios(request):
    Premios = Activbcn.objects.raw('SELECT * FROM TFM1app_Activbcn WHERE  tipo  like "Premios%" ')
    return render(request, 'TFM1app/Premios_barcelona.html', {'Premios': Premios})

def Por_tipo_Religiosos(request):
    Religiosos = Activbcn.objects.raw('SELECT * FROM TFM1app_Activbcn WHERE  tipo  like "Religiosos%" ')
    return render(request, 'TFM1app/Religiosos.html', {'Religiosos': Religiosos})

def Por_tipo_Solidaridad(request):
    Solidaridad = Activbcn.objects.raw('SELECT * FROM TFM1app_Activbcn WHERE  tipo  like "Solidaridad%" ')
    return render(request, 'TFM1app/Solidaridad_barcelona.html', {'Solidaridad': Solidaridad})

def Por_tipo_Teatro(request):
    Teatros = Activbcn.objects.raw('SELECT * FROM TFM1app_Activbcn WHERE  tipo  like "Teatro%" ')
    return render(request, 'TFM1app/Teatros_barcelona.html', {'Teatros': Teatros})

def Por_tipo_Visitas(request):
    Visitas = Activbcn.objects.raw('SELECT * FROM TFM1app_Activbcn WHERE  tipo  like "Visitas%" ')
    return render(request, 'TFM1app/Visitas_barcelona.html', {'Visitas': Visitas})