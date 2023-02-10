from django.shortcuts import render
from .models import Department, Employees
from .serializer import EmployeesSerializer
from rest_framework.response import Response

# Create your views here.
def home(request):
     employees = Employees.objects.all().select_related("department")
     # serializer = EmployeesSerializer(employees, many=True)
     # return Response(serializer.data)

     # for employee in employees:
     #      print(employee.name, employee.department.name)