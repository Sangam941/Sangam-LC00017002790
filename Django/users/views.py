from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Users
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

# Create your views here.
def create(request):
    return HttpResponse("this is a create page")

class UserViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def delete(self, request, *args, **kwrgs):
        Users.objects.all().delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

# class UsersCreateList(generics.ListCreateAPIView):
#     queryset = Users.objects.all()
#     serializer_class = UserSerializer

#     def delete(self, request, *args, **kwrgs):
#         Users.objects.all().delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)

# class UserUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Users.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'pk'