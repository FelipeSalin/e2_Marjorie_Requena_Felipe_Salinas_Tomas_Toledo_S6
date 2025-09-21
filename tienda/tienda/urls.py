"""
URL configuration for tienda project.

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
from django.contrib import admin
from django.urls import path

from core.views import index_estatico, contacto, audio, bateria, cableado, carcasas, soporte, compra, pago, inventario, formulario_ingreso, formulario_modificacionperfil, formulario_pwolvidada, formulario_recuperarpw, formulario_registro

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index_estatico, name="index"),
    path("contacto/", contacto, name="contacto"),
    path("audio/", audio, name="audio"),
    path("bateria/", bateria, name="bateria"),
    path("cableado/", cableado, name="cableado"),
    path("carcasas/", carcasas, name="carcasas"),
    path("soporte/", soporte, name="soporte"),
    path("compra/", compra, name="compra"),
    path("pago/", pago, name="pago"),
    path("registro_inventario/", inventario, name="inventario"),
    path("formulario_ingreso/", formulario_ingreso, name="formulario_ingreso"),
    path("formulario_modificacionperfil/", formulario_modificacionperfil, name="formulario_modificacionperfil"),
    path("formulario_pwolvidada/", formulario_pwolvidada, name="formulario_pwolvidada"),
    path("formulario_recuperarpw/", formulario_recuperarpw, name="formulario_recuperarpw"),
    path("formulario_registro/", formulario_registro, name="formulario_registro"),
    path("login/",ejemplo,name="login"),
]