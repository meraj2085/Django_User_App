from django.urls import path
from . import views

urlpatterns = [
     path('reporter', views.AddReporter),
     path('article', views.AddArticle),
]