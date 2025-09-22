from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__ (self):
        return self.nombre

class Producto(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to="productos/", null=True, blank=True, default="default.jpg")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    
    def __str__ (self):
        return self.nombre
    
class Inventario(models.Model):
    nombre = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=50, unique=True)  # mejor CharField
    cantidad = models.PositiveIntegerField()  
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.nombre} ({self.cantidad})"
    
"""
class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=settings.ROLES)

    def __str__(self):
        return self.user.username + ' - ' + self.role
"""