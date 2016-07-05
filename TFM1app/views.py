from django.shortcuts import render
from .models import Activmad
import requests


def Activ_listmad(request):

    Activmads=Activmad.objects.all()   
    return render(request, 'TFM1app/Activ_listMad.html', {'Activmads': Activmads})