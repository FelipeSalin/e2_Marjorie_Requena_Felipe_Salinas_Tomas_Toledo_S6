import requests

from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.models import Categoria, Producto, Inventario
from .serializers import CategoriaSerializer, ProductoSerializer, InventarioSerializer

from requests.adapters import HTTPAdapter, Retry
import time
import logging

# Create your views here.

#Listas de los modelos (GET, POST)



logger = logging.getLogger(__name__)

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def lista_Categoria(request):
    if request.method == 'GET':
        start_time = time.time()

        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria, many=True)

        duration = time.time() - start_time
        if duration > 2:  # si tarda más de 2 segundos
            logger.warning(f"La consulta de categorías tardó {duration:.2f} segundos")

        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(data = data) #revisar BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        
@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def lista_Producto(request):
    if request.method == 'GET':
        start_time = time.time()

        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)

        duration = time.time() - start_time
        if duration > 2:  # si tarda más de 2 segundos
            logger.warning(f"La consulta de productos tardó {duration:.2f} segundos")

        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data = data) #revisar BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def lista_Inventario(request):
    if request.method == 'GET':
        start_time = time.time()

        inventario = Inventario.objects.all()
        serializer = InventarioSerializer(inventario, many=True)

        duration = time.time() - start_time
        if duration > 2:  # si tarda más de 2 segundos
            logger.warning(f"La consulta de inventario tardó {duration:.2f} segundos")

        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = InventarioSerializer(data = data) #revisar BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

#Detalles de los modelos (GET, PUT, DELETE)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalle_Categoria(request, id):
    try:
        m = Categoria.objects.get(id = id) #ver BD
    except Categoria.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        start_time = time.time()

        serializer = CategoriaSerializer(m)

        duration = time.time() - start_time
        if duration > 2:  # si tarda más de 2 segundos
            logger.warning(f"La consulta de detalle categoría tardó {duration:.2f} segundos")

        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(m, data = data) #ver BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalle_Producto(request, id):
    try:
        m = Producto.objects.get(id = id) #ver BD
    except Producto.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        start_time = time.time()

        serializer = ProductoSerializer(m)

        duration = time.time() - start_time
        if duration > 2:  # si tarda más de 2 segundos
            logger.warning(f"La consulta de detalle producto tardó {duration:.2f} segundos")

        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(m, data = data) #ver BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalle_Inventario(request, id):
    try:
        m = Inventario.objects.get(id = id) #ver BD
    except Inventario.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        start_time = time.time()

        serializer = InventarioSerializer(m)

        duration = time.time() - start_time
        if duration > 2:  # si tarda más de 2 segundos
            logger.warning(f"La consulta de detalle inventario tardó {duration:.2f} segundos")

        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = InventarioSerializer(m, data = data) #ver BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


#APIS EXTERNAS
def consumir_api_externa(method, url, headers=None, payload=None):
    try:
        session = requests.Session()
        retries = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[500, 502, 503, 504],
        )
        session.mount('http://', HTTPAdapter(max_retries=retries))
        session.mount('https://', HTTPAdapter(max_retries=retries))

        timeout = (5, 10)

        if method.upper() == 'GET':
            response = session.get(url, headers=headers, timeout=timeout)
        elif method.upper() == 'POST':
            response = session.post(url, headers=headers, json=payload, timeout=timeout)
        else:
            return {"error": "Método HTTP no soportado."}

        response.raise_for_status()  # Lanza error si status_code >= 400
        return response.json()

    except requests.Timeout:
        return {"error": "El servicio tardó demasiado en responder. Intente nuevamente más tarde."}
    except requests.ConnectionError:
        return {"error": "No se pudo conectar al servicio. Revise su conexión a internet."}
    except requests.HTTPError as e:
        return {"error": f"Error HTTP: {e.response.status_code} - {e.response.reason}"}
    except Exception as e:
        return {"error": f"Ocurrió un error inesperado: {str(e)}"}
    


@api_view(['GET'])
def dispositivos(request):
    url = "https://mobile-phone-specs-database.p.rapidapi.com/gsm/get-specifications-by-phone-custom-id/103693"

    headers = {
	"x-rapidapi-key": "57207918e5msh0630f5103bb193dp15ee30jsn6be1cce08a90",
	"x-rapidapi-host": "mobile-phone-specs-database.p.rapidapi.com"
    }

    data = consumir_api_externa('GET', url, headers=headers)

    return Response(data)


@api_view(['GET'])
def generarqr(request):
    url = "https://qr-generator26.p.rapidapi.com/api/generate"

    payload = {
        "text": "https://youtube.com",
        "format": "base64"
    }
    headers = {
        "x-rapidapi-key": "57207918e5msh0630f5103bb193dp15ee30jsn6be1cce08a90",
        "x-rapidapi-host": "qr-generator26.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    data = consumir_api_externa('POST', url, headers=headers, payload=payload)

    return Response(data)