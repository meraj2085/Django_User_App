from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import UserSerializer
from .models import Users
# import json


# Create your views here.
@api_view(['GET', 'POST'])
def Users_list(request, format=None):
     try:
          if request.method == 'GET':
               users = Users.objects.all()
               serializer = UserSerializer(users, many=True)
               return Response(serializer.data)
          elif request.method == 'POST':
               print(request.data)
               serializer = UserSerializer(data=request.data)
               if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
     except Exception:
          Response(Exception)

@api_view(['GET', 'PUT', 'DELETE'])
def User_Details(request, id, format=None):
     try:
          user = Users.objects.get(pk=id)
     except Users.DoesNotExist:
          return Response(status=status.HTTP_404_NOT_FOUND)


     if request.method == 'GET':
          serializer = UserSerializer(user)
          return Response(serializer.data)
     elif request.method == 'PUT':
          serializer = UserSerializer(user, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     elif request.method == 'DELETE':
          user.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)