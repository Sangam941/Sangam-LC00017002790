from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Users
from .serializers import UserSerializer
from .permissions import IsAdminOrReadOnly

# Create your views here.



class UserViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]

    def delete(self, request, *args, **kwrgs):
        Users.objects.all().delete()
        return Response(status = status.HTTP_204_NO_CONTENT)