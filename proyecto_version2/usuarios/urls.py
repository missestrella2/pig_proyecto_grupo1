from django.urls import path, re_path #segun clase 10
from . import views #segun clase 10 significa: desde donde estoy importa las vistas
from django import forms

urlpatterns=[

    path('usuarios/usuariosform',views.usuariosform,name="usuariosform"),
    path('usuarios/altausuarioform',views.altausuarioform,name="altausuarioform"),
    path('usuarios/bajausuarioform',views.bajausuarioform,name="bajausuarioform"),
    path('usuarios/resultadoalta/',views.resultadoalta,name="resultadoalta"),
    path('usuarios/resultadobaja/',views.resultadobaja,name="resultadobaja"),
    path('usuarios/resultadofiltro/',views.resultadofiltro,name="resultadofiltro"),

#ejemplo formulario
    path('usuarios/busqueda_productos/',views.busqueda_productos,name="busqueda_productos"),
    path('usuarios/buscar/',views.buscar,name="buscar"),
 
]

