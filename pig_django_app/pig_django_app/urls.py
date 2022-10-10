"""pig_django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import include #segun clase 10 necesito importar el include para poder conectar
                                #este archivo url con las url de las app
#from prueba_clientes import views  #segun clase 10 asi importo las vistas de "prueba clientes"
from prueba_clientes import views #aca importar la app que tenga el index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba_clientes/',include('prueba_clientes.urls')), #asi conecto urls con el urls dentro de la app
    path('prueba_productos/',include('prueba_productos.urls')),
    path('',views.index), #entra a la funcion index de las views de prueba clientes 
]
