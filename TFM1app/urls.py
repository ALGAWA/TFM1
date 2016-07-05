from django.conf.urls import url
from . import views, viewbcn,viewIndex, viewfiltros
from . import viewfiltrosbcn, viewActualizarbcn, ActualizarMad
from TFM1app import viewIndexCreate, viewCrearmadrid, viewCrearbcn, viewsActualiza




urlpatterns = [


url(r'^([\D]+)/$',viewfiltros.Por_tipo, name='Por_tipo'),
url(r'^([\D]+)/b$',viewfiltrosbcn.Por_tipo, name='Por_tipo'),


url(r'^crea/mad$', viewCrearmadrid.Crear_mad, name='Crear_mad'),
url(r'^crea/bcn$',viewCrearbcn.Crear_bcn, name='Crear_bcn'),
url(r'^crea$', viewIndexCreate.IndexCrear, name='IndexCrear'),
url(r'^mad$', views.Activ_listmad, name='Activ_listmad'),
url(r'^bcn$',viewbcn.Activ_listbcn, name='Activ_listbcn'),
url(r'^actua$', viewsActualiza.IndexAdmin, name='IndexAdmin'),
url(r'^actua/mad$', ActualizarMad.Actualizar_mad, name='Actualizar_mad'),
url(r'^actua/bcn$',viewActualizarbcn.Obtenerdatosbcn, name='Obtenerdatosbcn'),


url(r'^musica$',viewfiltros.Por_tipo_Musica, name='Por_tipo_Musica'),
url(r'^cine$',viewfiltros.Por_tipo_cine, name='Por_tipo_cine'),
url(r'^fiestas$',viewfiltros.Por_tipo_Fiestas, name='Por_tipo_Fiestas'),
url(r'^cuentos$',viewfiltros.Por_tipo_CuentaCuentos, name='Por_tipo_CuentaCuentos'),
url(r'^comemoraciones$',viewfiltros.Por_tipo_ComemoracionesHomenajes, name='Por_tipo_ComemoracionesHomenajes'),
url(r'^destacada$',viewfiltros. Por_tipo_ProgramacionDestacada, name=' Por_tipo_ProgramacionDestacada'),
url(r'^danza$',viewfiltros.Por_tipo_Danza, name='Por_tipo_Danza'),
url(r'^conferencias$',viewfiltros.Por_tipo_Conferencias, name='Por_tipo_Conferencias'),
url(r'^talleres$',viewfiltros.Por_tipo_CursosTalleres, name='Por_tipo_CursosTalleres'),
url(r'^actividades$',viewfiltros.Por_tipo_Actividades, name='Por_tipo_Actividades'),
url(r'^circo$',viewfiltros.Por_tipo_Circo, name='Por_tipo_Circo'),
url(r'^concursos$',viewfiltros.Por_tipo_Cocursos, name='Por_tipo_Cocursos'),
url(r'^congresos$',viewfiltros.Por_tipo_Congresos, name='Por_tipo_Congresos'),
url(r'^excursiones$',viewfiltros.Por_tipo_Excursiones, name='Por_tipo_Excursiones'),
url(r'^ferias$',viewfiltros.Por_tipo_Ferias, name='Por_tipo_Ferias'),
url(r'^recitales$',viewfiltros.Por_tipo_Recitales, name='Por_tipo_Recitales'),
url(r'^exposiciones$',viewfiltros.Por_tipo_Exposiciones, name='Por_tipo_Exposiciones'),

url(r'^cinebarcelona$',viewfiltrosbcn.Por_tipo_cine, name='Por_tipoc_Cine'),
url(r'^coloniasbcn$',viewfiltrosbcn.Por_tipo_Colonias, name='Por_tipo_Colonias'),
url(r'^cogresosbcn$',viewfiltrosbcn.Por_tipo_Congresos, name='Por_tipo_Congresos'),
url(r'^deportesbcn$',viewfiltrosbcn.Por_tipo_Deportes, name='Por_tipo_Deportes'),
url(r'^Exposicionesbcn$',viewfiltrosbcn.Por_tipo_Exposiciones, name='Por_tipo_Exposiciones'),
url(r'^feriasbcn$',viewfiltrosbcn.Por_tipo_Ferias, name='Por_tipo_Ferias'),
url(r'^culturageneralbcn$',viewfiltrosbcn.Por_tipo_culturageneral, name='Por_tipo_culturageneral'),
url(r'^fiestasbcn$',viewfiltrosbcn.Por_tipo_Fiestas, name='Por_tipo_Fiestas'),
url(r'^juegosbcn$',viewfiltrosbcn. Por_tipo_Juegos, name=' Por_tipo_Juegos'),
url(r'^Literaturabcn$',viewfiltrosbcn.Por_tipo_Literatura, name='Por_tipo_Literatura'),
url(r'^modabcn$',viewfiltrosbcn.Por_tipo_Moda, name='Por_tipo_Moda'),
url(r'^musicbcn$',viewfiltrosbcn.Por_tipo_Musica, name='Por_tipo_Musica'),
url(r'^ninosbcn$',viewfiltrosbcn.Por_tipo_Ninos, name='Por_tipo_Ninos'),
url(r'^premiosbcn$',viewfiltrosbcn.Por_tipo_Premios, name='Por_tipo_Premios'),
url(r'^religiososbcn$',viewfiltrosbcn.Por_tipo_Religiosos, name='Por_tipo_Religiosos'),
url(r'^solidaridadbcn$',viewfiltrosbcn.Por_tipo_Solidaridad, name='Por_tipo_Solidaridad'),
url(r'^teatrobcn$',viewfiltrosbcn.Por_tipo_Teatro, name='Por_tipo_Teatro'),
url(r'^visitasbcn$',viewfiltrosbcn.Por_tipo_Visitas, name='Por_tipo_Visitas'),

url(r'', viewIndex.Index, name='Index')
]


   

    


