import datetime
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

"""
for user in User.objects.all():
    Token.objects.get_or_create(user=user)
"""
"""
from rest_framework.permissions import IsAuthenticated
class MiVistaProtegida(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
"""

"""
@api_view(['POST'])
@permission_classes([AllowAny])  # Permitir login sin autenticación previa
def login(request):
    data = request.data  # DRF ya parsea JSON automáticamente

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return Response(
            {"error": "Debe ingresar username y password"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        user = User.objects.get(username = username) #revisar en BD
    except User.DoesNotExist:
        return Response(
            {"error": "Usuario incorrecto"},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    # Validación de contraseña
    if not check_password(password, user.password):
        return Response(
            {"error": "Contraseña incorrecta"},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    # Crear o recuperar token
    token, created = Token.objects.get_or_create(user=user)
    return Response(
        {"token": token.key},
        status=status.HTTP_200_OK
    )
"""

@csrf_exempt
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username is None or password is None:
        return Response({
            'success': False,
            'message': 'Username y password son requeridos',
            'data': {},
            'time': datetime.datetime.now(),
        }, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=username, password=password)

    if user:
        token, created = Token.objects.get_or_create(user=user)
        respuesta = {
            'success': True,
            'messagge': 'Login exitoso',
            'token': token.key,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            },
            'time': datetime.datetime.now(),
        }
        return Response(respuesta)
    else:
        return Response({
            'success': False,
            'message': 'Credenciales inválidas',
            'data': {},
            'time': datetime.datetime.now(),
        }, status=status.HTTP_401_UNAUTHORIZED)
      

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def perfil_usuario(request):
    user = request.user
    respuesta = {
        'success': True,
        'message': 'Perfil del usuario autenticado',
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
        },
        'time': datetime.datetime.now(),
    }
    return Response(respuesta)