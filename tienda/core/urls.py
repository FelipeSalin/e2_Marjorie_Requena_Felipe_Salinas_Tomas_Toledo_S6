from django.urls import path, include
from . import views
from rest_api import viewsLogin

app_name = "core"

urlpatterns = [
    path('api/', include('rest_api.urls')),
]