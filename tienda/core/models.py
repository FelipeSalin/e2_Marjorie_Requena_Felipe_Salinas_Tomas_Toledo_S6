from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__ (self):
        return self.nombre

class Producto(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    
    def __str__ (self):
        return self.nombre
    
    class Inventario(models.Model):
        nombre = models.CharField(max_length=100)
        identificacion = models.CharField(max_length=50, unique=True)  
        cantidad = models.PositiveIntegerField()  
        categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.nombre} ({self.cantidad})"
    

    