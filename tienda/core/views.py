from django.shortcuts import render

# Create your views here.
def index_estatico(request):
    return render(request, "index.html")

def contacto(request):
    return render(request, "contacto.html")

def audio(request):
    return render(request, "categorias/audio.html")

def bateria(request):
    return render(request, "categorias/bateria.html")

def cableado(request):
    return render(request, "categorias/cableado.html")

def carcasas(request):
    return render(request, "categorias/carcasas.html")

def soporte(request):
    return render(request, "categorias/soporte.html")

def compra(request):
    return render(request, "compras/compra.html")

def pago(request):
    return render(request, "compras/pago.html")

def inventario(request):
    return render(request, "compras/registro_inventario.html")

def formulario_ingreso(request):
    return render(request, "formularios/formulario_ingreso.html")

def formulario_modificacionperfil(request):
    return render(request, "formularios/formulario_modificacionperfil.html")

def formulario_pwolvidada(request):
    return render(request, "formularios/formulario_pwolvidada.html")

def formulario_recuperarpw(request):
    return render(request, "formularios/formulario_recuperarpw.html")

def formulario_registro(request):
    return render(request, "formularios/formulario_registro.html")