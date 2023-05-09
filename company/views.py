from django.shortcuts import render
from .models import Department, Employees
from .serializer import EmployeesSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
import json
import requests
import random
import http.client

# Create your views here.
def home(request):
     employees = Employees.objects.select_related("department").filter(id=1)
     list = []

     for employee in employees:
          list.append({'id':employee.id, 'name':employee.name, 'age': employee.age, 'department_name': employee.department.name})

     return HttpResponse(json.dumps(list[0]))



@api_view(['GET'])
def Send_OTP(request):
    try:
        mobile = request.data['mobile_number']
        otp = random.randint(1000, 9999)

        # Send SMS using Msg91 API
        api_key = "394026ANmKefWqb642cf6f8P1"
        phone_number = mobile
        message = f"Your OTP is {otp}."
        send_sms(api_key, phone_number, message)

        return Response({"success": True, 'OTP': otp, "message": "OTP sent successfully"}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({'error': "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def send_sms(api_key, phone_number, message):
    url = "https://api.msg91.com/api/sendhttp.php"
    payload = {
        "authkey": api_key,
        "mobiles": phone_number,
        "message": message,
        "sender": "smsind",
        "route": "4"
    }
    response = requests.get(url, params=payload)
    return response.text


