from django.conf.urls import url
from . import views, viewbcn,wievindex, viewfiltros, viewfiltrosbcn


urlpatterns = [
url(r'mad', views.Activ_listmad, name='Activ_listmad'),
url(r'bcn',viewbcn.Activ_listbcn, name='Activ_listbcn'),

url(r'musica',viewfiltros.Por_tipo_Musica, name='Por_tipo_Musica'),
url(r'cine',viewfiltros.Por_tipo_cine, name='Por_tipo_cine'),
url(r'fiestas',viewfiltros.Por_tipo_Fiestas, name='Por_tipo_Fiestas'),
url(r'cuentos',viewfiltros.Por_tipo_CuentaCuentos, name='Por_tipo_CuentaCuentos'),
url(r'comemoraciones',viewfiltros.Por_tipo_ComemoracionesHomenajes, name='Por_tipo_ComemoracionesHomenajes'),
url(r'destacada',viewfiltros. Por_tipo_ProgramacionDestacada, name=' Por_tipo_ProgramacionDestacada'),
url(r'danza',viewfiltros.Por_tipo_Danza, name='Por_tipo_Danza'),
url(r'conferencias',viewfiltros.Por_tipo_Conferencias, name='Por_tipo_Conferencias'),
url(r'talleres',viewfiltros.Por_tipo_CursosTalleres, name='Por_tipo_CursosTalleres'),
url(r'actividad',viewfiltros.Por_tipo_Actividades, name='Por_tipo_Actividades'),
url(r'circo',viewfiltros.Por_tipo_Circo, name='Por_tipo_Circo'),
url(r'concursos',viewfiltros.Por_tipo_Cocursos, name='Por_tipo_Cocursos'),
url(r'congresos',viewfiltros.Por_tipo_Congresos, name='Por_tipo_Congresos'),
url(r'excursiones',viewfiltros.Por_tipo_Excursiones, name='Por_tipo_Excursiones'),
url(r'ferias',viewfiltros.Por_tipo_Ferias, name='Por_tipo_Ferias'),
url(r'recitales',viewfiltros.Por_tipo_Recitales, name='Por_tipo_Recitales'),
url(r'exposiciones',viewfiltros.Por_tipo_Exposiciones, name='Por_tipo_Exposiciones'),

url(r'cinebarcelona',viewfiltrosbcn.Por_tipo_cinebarcelona, name='Por_tipo_Cinebarcelona'),
url(r'coloniasbarcelona',viewfiltrosbcn.Por_tipo_Colonias, name='Por_tipo_Colonias'),
url(r'congresosbarcelona',viewfiltrosbcn.Por_tipo_Congresos, name='Por_tipo_Congresos'),
url(r'deportesbarcelona',viewfiltrosbcn.Por_tipo_Deportes, name='Por_tipo_Deportes'),
url(r'Exposicionesbarcelona',viewfiltrosbcn.Por_tipo_Exposiciones, name='Por_tipo_Exposiciones'),
url(r'feriasbarcelona',viewfiltrosbcn.Por_tipo_Ferias, name='Por_tipo_Ferias'),
url(r'fiestasbarcelona',viewfiltrosbcn.Por_tipo_Fiestas, name='Por_tipo_Fiestas'),
url(r'juegosbarcelona',viewfiltrosbcn. Por_tipo_Juegos, name=' Por_tipo_Juegos'),
url(r'literaturabarcelona',viewfiltrosbcn.Por_tipo_Literatura, name='Por_tipo_Literatura'),
url(r'modabarcelona',viewfiltrosbcn.Por_tipo_Moda, name='Por_tipo_Moda'),
url(r'musicabarcelona',viewfiltrosbcn.Por_tipo_Musica, name='Por_tipo_Musica'),
url(r'ninosbarcelona',viewfiltrosbcn.Por_tipo_Ninos, name='Por_tipo_Ninos'),
url(r'premiosbarcelona',viewfiltrosbcn.Por_tipo_Premios, name='Por_tipo_Premios'),
url(r'religiososbarcelona',viewfiltrosbcn.Por_tipo_Religiosos, name='Por_tipo_Religiosos'),
url(r'solidaridadbarcelona',viewfiltrosbcn.Por_tipo_Solidaridad, name='Por_tipo_Solidaridad'),
url(r'teatrobarcelona',viewfiltrosbcn.Por_tipo_Teatro, name='Por_tipo_Teatro'),
url(r'visitasbarcelona',viewfiltrosbcn.Por_tipo_Visitas, name='Por_tipo_Visitas'),


url(r'', wievindex.Index, name='Index')
]


   

    


