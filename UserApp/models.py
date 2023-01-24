from django.db import models

# Create your models here.
class Users(models.Model):
     UserId = models.AutoField(primary_key=True)
     UserName = models.CharField(max_length=100)
     UserEmail = models.CharField(max_length=100, unique = True)