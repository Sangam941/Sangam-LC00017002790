from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import Users
from .serializers import UserSerializer

# Create your views here.
def create(request):
    return HttpResponse("this is a create page")

class UsersCreateList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer