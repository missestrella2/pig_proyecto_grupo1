from django.urls import path
from . import views 

urlpatterns=[

    path('clientes/',views.clientes, name="clientes"),
    path('clientes/clientes-listado-completo',views.clientes_listado_completo, name="clientes_listado_completo"),
    path('clientes/altaclientes',views.altaclientes, name="altaclientes"),
    path('clientes/bajaclientes',views.bajaclientes, name="bajaclientes"),


    #path('clientes/2020',views.clientes_por_anio_de_alta, name="clientes_por_anio_de_alta")

    path('clientes/<int:anio>',views.clientes_por_anio_de_alta, name="clientes_por_anio_de_alta"),
    
]