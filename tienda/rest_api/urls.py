from django.urls import path
from . import views
from rest_api.viewsLogin import login, perfil_usuario

urlpatterns = [
    path('categorias/', views.lista_Categoria, name = "lista_Categoria"),
    path('productos/', views.lista_Producto, name = "lista_Producto"),
    path('inventario/', views.lista_Inventario, name = "lista_Inventario"),
    path('categorias/<int:id>/', views.detalle_Categoria, name = "detalle_Categoria"),
    path('productos/<int:id>/', views.detalle_Producto, name = "detalle_Producto"),
    path('inventario/<int:id>/', views.detalle_Inventario, name = "detalle_Inventario"),
    path('auth/login/', login, name = "login"),
    path('auth/perfil/', perfil_usuario, name = "perfil"),
]