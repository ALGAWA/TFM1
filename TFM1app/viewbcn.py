# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Activbcn



def Activ_listbcn(request):
    
    Activbcns=Activbcn.objects.all()   
    return render(request, 'TFM1app/Activ_listbcn.html', {'Activbcns' : Activbcns})
