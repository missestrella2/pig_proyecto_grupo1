from django.conf import settings
#from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

from django.urls import path,include

urlpatterns=[

    path('',views.index,name="index"), 
    path('paginaenblanco2/',login_required(views.paginaenblanco2),name="paginaenblanco2"),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.login, name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

]