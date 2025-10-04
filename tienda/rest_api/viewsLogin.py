import datetime
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated


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