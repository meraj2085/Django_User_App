from django.urls import path
from . import views

urlpatterns = [
     path('users/', views.Users_list),
     path('users/<int:id>', views.User_Details)
]