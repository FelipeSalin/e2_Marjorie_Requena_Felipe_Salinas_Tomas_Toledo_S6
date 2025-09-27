from django.urls import path
from . import views

urlpatterns = [
    path('categoria', views.listado_categorias, name='listado_categorias'),
    path('libro/<int:id>/editar/', views.editar_categoria, name='editar_categoria'),
]