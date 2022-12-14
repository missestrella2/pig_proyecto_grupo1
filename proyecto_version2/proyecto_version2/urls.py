"""proyecto_version2 URL Configuration

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
from django.conf.urls.static import static

from django.urls import include #segun clase 10 necesito importar el include para poder conectar
                                #este archivo url con las url de las app
#from prueba_clientes import views  #segun clase 10 asi importo las vistas de "prueba clientes"
from login import views #aca importar la app que tenga el index


from django.conf import settings

from django.urls import path,include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [

     path('', include('historial_ventas.urls')),
     path('', include('login.urls')),
     path('', include('estadisticas.urls')),
     path('', include('usuarios.urls')),


    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
