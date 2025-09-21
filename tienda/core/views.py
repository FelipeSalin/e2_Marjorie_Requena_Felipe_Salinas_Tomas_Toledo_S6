from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

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


#Autentificacion
def iniciar_sesion(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)  
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get("usuarioLogin")
            contrasena = formulario.cleaned_data.get("passLogin")
            usuario = authenticate(usuarioLogin=nombre_usuario, passLogin=contrasena)
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
            contexto = {
                "formulario": formulario
            }
            return render(request, "autenticacion/registro.html", contexto)
    else:
        formulario = CustomUserCreationForm()
        contexto = {
            "formulario": formulario
        }
        return render(request, "autenticacion/registro.html", contexto)

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect("index")
