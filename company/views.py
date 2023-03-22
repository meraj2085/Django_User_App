from django.shortcuts import render
from .models import Department, Employees
from .serializer import EmployeesSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
import json

# Create your views here.
def home(request):
     employees = Employees.objects.select_related("department").filter(id=1)
     print(employees)
     list = []

     for employee in employees:
          list.append({'id':employee.id, 'name':employee.name, 'age': employee.age, 'department_name': employee.department.name})

     return HttpResponse(json.dumps(list[0]))
