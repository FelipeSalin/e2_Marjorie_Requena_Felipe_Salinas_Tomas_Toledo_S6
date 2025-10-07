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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from core import views


from core.views import index_estatico, contacto, audio, bateria, cableado, carcasas, soporte, compra, pago, inventario, formulario_modificacionperfil, formulario_pwolvidada, formulario_recuperarpw, iniciar_sesion, cerrar_sesion, registro_usuario, mostrar

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('core.urls')),
    path("", index_estatico, name="index"),
    path('categoria/<int:id>', mostrar, name="mostrar"),
    path("productos/", views.mostrar_productos, name="mostrar_productos"),
    path("inventario/", views.mostrar_inventario, name="mostrar_inventario"),
    path("contacto/", contacto, name="contacto"),
    path("audio/", audio, name="audio"),
    path("bateria/", bateria, name="bateria"),
    path("cableado/", cableado, name="cableado"),
    path("carcasas/", carcasas, name="carcasas"),
    path("soporte/", soporte, name="soporte"),
    path("compra/", compra, name="compra"),
    path("pago/", pago, name="pago"),
    path("registro_inventario/", inventario, name="inventario"),
    path("formulario_modificacionperfil/", formulario_modificacionperfil, name="formulario_modificacionperfil"),
    path("formulario_pwolvidada/", formulario_pwolvidada, name="formulario_pwolvidada"),
    path("formulario_recuperarpw/", formulario_recuperarpw, name="formulario_recuperarpw"),
    path("login/", iniciar_sesion, name="login"),
    path("logout/", cerrar_sesion, name="logout"),
    path("registro/", registro_usuario, name="registro_usuario"),
    path("api/", include('rest_api.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#Se agrega lo anterior para darle el directorio, y para eso hay que configurar settings.py

#En el bloque de importaciones de settings.py, de agrega: import os

#Al final de settings.py, luego de DEFAULT_AUTO_FIELD, se debe agregar lo siguiente:
#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')