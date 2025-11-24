"""
URL configuration for django_project_allauth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
#JOSE GUADALUPE NEGRETE HERNANDEZ
from django.contrib import admin
from django.urls import path, include #Add Include
from django.views.generic import TemplateView #Add Para mostrar home.html
urlpatterns = [
    path("admin/", admin.site.urls),

    #Agregar:
    # Rutas de Django Allauth (Login, Logout, Signup, Password Reset/Change)
    path('accounts/', include('allauth.urls')),
    
    # Ruta principal (Home) usando la plantilla que creamos en el Paso 9
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
