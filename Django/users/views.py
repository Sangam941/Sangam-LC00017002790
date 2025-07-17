from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Users
from .serializers import UserSerializer

# Create your views here.
def create(request):
    return HttpResponse("this is a create page")

class UsersCreateList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, *args, **kwrgs):
        Users.objects.all().delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class UserUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'