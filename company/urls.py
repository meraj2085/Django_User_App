from django.urls import path
from . import views

urlpatterns = [
     path('employee', views.home),
     path('send_otp', views.Send_OTP),
]