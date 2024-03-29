from django.db import models

# Create your models here.
class Department(models.Model):
     name = models.CharField(max_length=50)
     
     def __str__(self):
          return self.name

class Employees(models.Model):
     name = models.CharField(max_length=125)
     age = models.IntegerField()
     department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="employees")

     def __str__(self):
          return self.name