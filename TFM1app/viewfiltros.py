from django.shortcuts import render
from .models import Activmad




def Por_tipo(request, tipo):
    Actividades = Activmad.objects.filter(  tipo  = tipo )
    return render(request, "TFM1app/Activ.html", {'Actividades': Actividades})

def Por_tipo_Musica(request):
    Musicas = Activmad.objects.raw('SELECT * FROM TFM1app_Activmad WHERE  tipo  like "Musica%" ')
    return render(request, 'TFM1app/Musica_madrid.html', {'Musicas': Musicas})


def Por_tipo_cine(request):
    Cines = Activmad.objects.raw('SELECT * FROM TFM1app_Activmad WHERE  tipo  like "Cine%" ')
    return render(request, 'TFM1app/Cine_madrid.html', {'Cines': Cines})

def Por_tipo_Fiestas(request):
    Fiestas = Activmad.objects.raw('SELECT * FROM TFM1app_Activmad WHERE  tipo  like "Fiestas%" ')
    return render(request, 'TFM1app/Fiestas_madrid.html', {'Fiestas': Fiestas})

def Por_tipo_CuentaCuentos(request):
    Cuentos = Activmad.objects.raw('SELECT * FROM TFM1app_Activmad WHERE  tipo  like "CuentaCuentos%" ')
    return render(request, 'TFM1app/Cuentacuentos.html', {'Cuentos': Cuentos})


def Por_tipo_ComemoracionesHomenajes(request):
    Comemoraciones = Activmad.objects.raw('SELECT * FROM TFM1app_Activmad WHERE  tipo  like "ComemoracionesHomenajes%" ')
    return render(request, 'TFM1app/Comemoraciones_madrid.html', {'Comemoraciones': Comemoraciones})

def Por_tipo_ProgramacionDestacada(request):
    Destacadas = Activmad.objects.raw('SELECT * FROM TFM1app_Activmad WHERE  tipo  like "ProgramacionDestacada%" ')
    return render(request, 'TFM1app/Destacadas_madrid.html', {'Destacadas': Destacadas})


def Por_tipo_Danza(request):
    Danzas = Activmad.objects.raw('SELECT * FROM TFM1app_Activmad WHERE  tipo  like "Danza%" ')
    return render(request, 'TFM1app/Danzas_madrid.html', {'Danzas': Danzas})

def Por_tipo_Conferencias(request):
    Conferencias = Activmad.objects.raw('SELECT * FROM TFM1app_Activmad WHERE  tipo  like "Conferencias%" ')
    return render(request, 'TFM1app/Conferencias_madrid.html', {'Conferencias': Conferencias})

def Por_tipo_CursosTalleres(request):
    CursosTalleres = Activmad.objects.raw('SELECT * FROM TFM1app_Activmad WHERE  tipo  like "CursosTalleres%" ')
    return render(request, 'TFM1app/CursosTalleres.html', {'CursosTalleres': CursosTalleres})


def Por_tipo_Actividades(request):
    Actividades = Activmad.objects.raw('SELECT * FROM TFM1app_Activmad WHERE  tipo  like "Actividades%" ')
    return render(request, 'TFM1app/Actividades.html', {'Actividades': Actividades})

def Por_tipo_Circo(request):
    Circos = Activmad.objects.raw('SELECT * FROM TFM1app_Activmad WHERE  tipo  like "Circo%" ')
    return render(request, 'TFM1app/Circos_madrid.html', {'Circos': Circos})

def Por_tipo_Cocursos(request):
    Concursos = Activmad.objects.raw('SELECT * FROM TFM1app_Activmad WHERE  tipo  like "Concursos%" ')
    return render(request, 'TFM1app/Concursos_madrid.html', {'Concursos': Concursos})

def Por_tipo_Congresos(request):
    Congresos = Activmad.objects.raw('SELECT * FROM TFM1app_Activmad WHERE  tipo  like "Congresos%" ')
    return render(request, 'TFM1app/Congresos_madrid.html', {'Congresos': Congresos})

def Por_tipo_Excursiones(request):
    Excursiones = Activmad.objects.raw('SELECT * FROM TFM1app_Activmad WHERE  tipo  like "Excursiones%" ')
    return render(request, 'TFM1app/Excursiones.html', {'Excursiones': Excursiones})

def Por_tipo_Exposiciones(request):
    Exposiciones = Activmad.objects.raw('SELECT * FROM TFM1app_Activmad WHERE  tipo  like "Exposiciones%" ')
    return render(request, 'TFM1app/Exposiciones_madrid.html', {'Exposiciones': Exposiciones})

def Por_tipo_Ferias(request):
    Ferias = Activmad.objects.raw('SELECT * FROM TFM1app_Activmad WHERE  tipo  like "Ferias%" ')
    return render(request, 'TFM1app/Ferias_madrid.html', {'Ferias': Ferias})

def Por_tipo_Recitales(request):
    Recitales = Activmad.objects.raw('SELECT * FROM TFM1app_Activmad WHERE  tipo  like "Recitales%" ')
    return render(request, 'TFM1app/Recitales_madrid.html', {'Recitales': Recitales})
