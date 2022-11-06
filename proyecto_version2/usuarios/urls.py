from django.urls import path #segun clase 10
from . import views #segun clase 10 significa: desde donde estoy importa las vistas

urlpatterns=[

    path('usuarios/',views.usuarios,name="usuarios"),
    path('usuarios/usuariosform',views.usuariosform,name="usuariosform"),
    path('usuarios/altausuarioform',views.altausuarioform,name="altausuarioform"),
    path('usuarios/bajausuarioform',views.bajausuarioform,name="bajausuarioform"),
]