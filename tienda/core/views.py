from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import Categoria, Producto, Inventario


from rest_framework.decorators import api_view
from ..rest_api.serializers import CategoriaSerializer, ProductoSerializer, InventarioSerializer
from rest_framework.response import Response

# Create your views here.

def index_estatico(request):

    categorias = []

    categoria1 = { 'id': 1, 'nombre': 'Audio y Sonido', 'imagen': 'assets/images/audio-y-sonido/JBLFlip.webp' }
    categoria2 = { 'id': 2, 'nombre': 'Batería', 'imagen': 'assets/images/baterias-y-energia/CargadorSolarAnker.webp' }
    categoria3 = { 'id': 3, 'nombre': 'Cableado', 'imagen': 'assets/images/carga-y-cableado/CargadorSamsung.webp' }
    categoria4 = { 'id': 4, 'nombre': 'Carcasas', 'imagen': 'assets/images/carcasas/iphone/iphone16promax1.png' }
    categoria5 = { 'id': 5, 'nombre': 'Soporte', 'imagen': 'assets/images/soportes-y-monturas/SoporteLamicall.webp' }

    categorias.append(categoria1)
    categorias.append(categoria2)
    categorias.append(categoria3)
    categorias.append(categoria4)
    categorias.append(categoria5)

    contexto = {
        'saludo': '👋 Bienvenido',
        'categorias': categorias
    }
    return render(request, "index.html", contexto)



def mostrar(request, id):
    categorias = [
        { 'nombre': 'Audio y Sonido', 'imagen': 'assets/images/audio-y-sonido/JBLFlip.webp'},
        { 'nombre': 'Batería', 'imagen': 'assets/images/baterias-y-energia/CargadorSolarAnker.webp'},
        { 'nombre': 'Cableado', 'imagen': 'assets/images/carga-y-cableado/CargadorSamsung.webp'},
        { 'nombre': 'Carcasas', 'imagen': 'assets/images/carcasas/iphone/iphone16promax1.png'},
        { 'nombre': 'Soporte', 'imagen': 'assets/images/soportes-y-monturas/SoporteLamicall.webp'}
    ]

    if id >= 0 and id < len(categorias):
        contexto = {
            'categoria': categorias[id]
        }

        return render(request, 'mostrar.html', contexto)
    else:
        return redirect('index')
def mostrar_productos(request):
    productos = Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'core/mostrar_productos.html', datos)


def mostrar_inventario(request):
    inventario = Inventario.objects.all()
    datos = {
        'inventario': inventario
    }
    return render(request, 'core/mostrar_inventario.html', datos)


def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    context = {
        'categoria': categoria
    }

    return render(request, 'categoria/editar.html', context)


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

def formulario_modificacionperfil(request):
    return render(request, "formularios/formulario_modificacionperfil.html")

def formulario_pwolvidada(request):
    return render(request, "formularios/formulario_pwolvidada.html")

def formulario_recuperarpw(request):
    return render(request, "formularios/formulario_recuperarpw.html")




#Autentificacion
def iniciar_sesion(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)  
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get("username")
            contrasena = formulario.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contrasena)
            if usuario is None:
                context={
                "formulario": formulario,
                "error": "Usuario o contraseña incorrectos"
                }
                return render(request, "autenticacion/login.html", context) 
            else:
                login(request, usuario)
                return redirect("index")
        else:
            context={
                "formulario": formulario,
                "error": "Usuario o contraseña incorrectos"
            }
            return render(request, "autenticacion/login.html", context)  
        
    else:    
        formulario = AuthenticationForm()
        context ={
            "formulario": formulario
        }
        return render(request, "autenticacion/login.html", context)

def registro_usuario(request):
    if request.method == "POST":
        # formulario = UserCreationForm(request.POST)
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
        else:
            context = {
                "formulario": formulario
            }
            return render(request, "autenticacion/registro.html", context)
    else:
        formulario = CustomUserCreationForm()
        context = {
            "formulario": formulario
        }
        return render(request, "autenticacion/registro.html", context)

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect("index")



#Views de los CRUD
def listado_categorias(request):
    categorias = Categoria.objects.all() # select * from libro;
    
    context = {
        'categorias' : categorias
    }
    return render(request, 'categoria/index.html', context)




#Views de los API REST
@api_view(['GET'])
def listar_categorias(request):
    categorias = Categoria.objects.all()
    serializadas = CategoriaSerializer(categorias, many=True)
    respuesta = {
        'success': True,
        'messagge': 'Lista de categorías',
        'data': serializadas.data,
        'total': len(serializadas.data)
    }
    return Response(serializadas.data)

@api_view(['GET'])
def listar_productos(request):
    productos = Producto.objects.all()
    serializadas = ProductoSerializer(productos, many=True)
    return Response(serializadas.data)

@api_view(['GET'])
def listar_productos_por_categoria(request, categoria_id):
    try:
        categoria = Categoria.objects.get(id=categoria_id)

        productos = Producto.objects.filter(categoria_id=categoria_id)
        serializadas = ProductoSerializer(productos, many=True)
        return Response(serializadas.data)

    except Categoria.DoesNotExist:
        return Response({'error': 'Categoría no encontrada'}, status=404)

"""
#ejemplo ocupando request, que es (por lo que entiendo) con urls externas
@api_view(['GET'])
def noticias_juegos(request):
    response = requests.get(url="https://www.mmobomb.com/api1/latestnews")
    noticias = []
    if response.status_code == 200:
        noticias = response.json()
    return Response(noticias)

#ejemplo ocupando request, que es (por lo que entiendo) con urls externas
@api_view(['GET'])
def noticias_juegos(request):
    response = requests.get(url="https://www.mmobomb.com/api1/latestnews")
    noticias = []
    if response.status_code == 200:
        noticias = response.json()
    return Response(noticias)
"""