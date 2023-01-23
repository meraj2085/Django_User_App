from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Users
from .serializers import UserSerializer

# Create your views here.


@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = Users.objects.create(
            name=data['name'],
            email=data['email'],
            password=data['password'],
            phone_number=data['phone_number']
        )
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    except:
        message = {
            'message': 'User with this email or phone number already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
