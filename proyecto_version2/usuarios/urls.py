from django.urls import path, re_path
from . import views

urlpatterns=[

    #path('usuarios/usuariosform',views.usuariosform,name="usuariosform"),
    # path('usuarios/altausuarioform',views.altausuarioform,name="altausuarioform"),
    # path('usuarios/bajausuarioform',views.bajausuarioform,name="bajausuarioform"),
    
    # path('usuarios/resultadoalta/',views.resultadoalta,name="resultadoalta"),
    # path('usuarios/resultadobaja/',views.resultadobaja,name="resultadobaja"),
    # path('usuarios/resultadofiltro/',views.resultadofiltro,name="resultadofiltro"),

    path('usuarios/listadeusuarios/',views.ListaDeUsuarios.as_view(),name='listadeusuarios'),
    path('usuarios/altausuarioform', views.altausuarioform.as_view(), name='altausuarioform'),
    path('usuarios/bajausuarioform',views.bajausuarioform.as_view(),name="bajausuarioform"),
    path('usuarios/usuarioeditar/<int:id_usuario>',views.usuarioeditar,name='usuarioeditar'),
    path('usuarios/usuarioeliminar/<int:id_usuario>',views.usuarioeliminar,name='usuarioeliminar'),


]

