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

# Create your views here.

#Listas de los modelos (GET, POST)

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def lista_Categoria(request):
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria, many=True)
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
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
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
        inventario = Inventario.objects.all()
        serializer = InventarioSerializer(inventario, many=True)
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
        serializer = CategoriaSerializer(m)
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
        serializer = ProductoSerializer(m)
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
        serializer = InventarioSerializer(m)
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

@api_view(['GET'])
def dispositivos(request):
    url = "https://mobile-phone-specs-database.p.rapidapi.com/gsm/get-specifications-by-phone-custom-id/103693"

    headers = {
	"x-rapidapi-key": "57207918e5msh0630f5103bb193dp15ee30jsn6be1cce08a90",
	"x-rapidapi-host": "mobile-phone-specs-database.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    return Response(response.json())

@api_view(['GET'])
def supporter(request):
    url = "https://cybrix-bytedance1.p.rapidapi.com/captcha/whirl"

    payload = {
        "proxy": "username:password@host:port",
        "store_idc": "rc-verification16-normal-useast5.tiktokv.us",
        "device_data": {
            "is_activated": True,
            "install_id": "7483053014685697834",
            "device_id": "7483052853188871723",
            "new_user": True,
            "cookie": "store-idc=useast5;store-country-code=us;store-country-code-src=did;store-country-sign=MEIEDA1DtjiSl_cNNsHQZwQgxWPq3teJdyRSfXj_G6r06Oz9MyLLjLoxswIwd7bzwFwEED-TFrGPlYrBuw2IrFWXKUI;install_id=7483053014685697834;ttreq=1$82260851ed45b35967e3ba364358c44bcf7d669e;",
            "user_agent": "com.zhiliaoapp.musically/2023604020 (Linux; U; Android 9; zh_TW; UPlay; Build/PQ1A.190105.034; Cronet/TTNetVersion:f4207711 2024-10-08 QuicVersion:7f85cd2d 2025-02-20)",
            "device_info": {
                "iid": "7483053014685697834",
                "device_id": "7483052853188871723",
                "version_code": "360402",
                "os_version": "9",
                "app_name": "musical_ly",
                "device_platform": "android",
                "aid": "1233",
                "channel": "googleplay",
                "cdid": "3da904c6-2efc-8260-a8fa-23a9b52a8b14",
                "openudid": "b85a18cd9daf006e",
                "device_type": "UPlay",
                "device_brand": "HTC",
                "device_model": "UPlay",
                "os_api": 28,
                "dpi": 428,
                "ssmix": "a",
                "region": "US",
                "carrier_region": "US",
                "op_region": "US",
                "sys_region": "US",
                "residence": "US",
                "current_region": "US",
                "app_language": "en",
                "locale": "en",
                "language": "zh_TW",
                "timezone_offset": -14400,
                "manifest_version_code": 2023604020,
                "update_version_code": 2023604020,
                "app_type": "normal",
                "uoo": 0,
                "content_language": "zh_TW",
                "host_abi": "arm64-v8a",
                "version_name": "36.4.2",
                "ab_version": "36.4.2",
                "build_number": "36.4.2",
                "ac2": "wifi",
                "ac": "5g",
                "resolution": "1080*1920",
                "timezone_name": "America/New_York",
                "mcc_mnc": "310510",
                "carrier_region_v2": "310"
            },
            "mssdk_version_str": "v05.01.00-ov-android",
            "seed_data": "MDGkHZ7WrnYOITx4yTthlobjzuZzTiV3A2F/oP0HSUuDLBeFQzBrHVEoSB63NQOm2ekDJALOxhKdvA7OUKD0UgvDxjaMVrQFf4xnmkJB7jQxrMlFFu6yp38TZXjYvtfMBvE=",
            "seed_version": 2,
            "device_token": "A79bRfwg1rMRsrq9osIF6ozfn",
            "ri_report": True
        }
    }
    headers = {
        "x-rapidapi-key": "57207918e5msh0630f5103bb193dp15ee30jsn6be1cce08a90",
        "x-rapidapi-host": "cybrix-bytedance1.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    return Response(response.json())