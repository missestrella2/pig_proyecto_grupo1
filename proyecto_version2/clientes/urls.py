from django.urls import path #segun clase 10
from . import views #segun clase 10 significa: desde donde estoy importa las vistas

urlpatterns=[

    path('clientes/',views.clientes, name="clientes"),
    path('clientes/clientes-listado-completo',views.clientes_listado_completo, name="clientes_listado_completo"),
    # path('clientes/<int:year>',views.clientes_por_anio_de_alta, name="clientes_por_anio_de_alta"),
     path('clientes/2020',views.clientes_por_anio_de_alta, name="clientes_por_anio_de_alta")
]