from django.urls import path, include
from . import views
from rest_api import viewsLogin

app_name = "core"

urlpatterns = [
    #path('categoria', views.listado_categorias, name='listado_categorias'),
    #path('libro/<int:id>/editar/', views.editar_categoria, name='editar_categoria'),
    path('api/categorias', views.listar_categorias, name='listar_categorias'),
    path('api/productos', views.listar_productos, name='listar_productos'),
    path('api/productos/categoria/<int:categoria_id>', views.listar_productos_por_categoria, name='listar_productos_por_categoria'),
    path('api/auth/login', viewsLogin.login, name='login'),
    path('api/auth/perfil', viewsLogin.perfil_usuario, name='perfil'),
    #path('api/inventario', listar_inventario, name='listar_inventario'),
    path('api/', include('rest_api.urls'))
]