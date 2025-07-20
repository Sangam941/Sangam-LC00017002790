from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Vehicles
from .serializers import VehicleSerializer

# Create your views here.

def create(request):
    return HttpResponse("hello from home")

class UserViewset(viewsets.ModelViewSet):
    queryset = Vehicles.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [AllowAny]