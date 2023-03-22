from django.urls import path
from . import views

urlpatterns = [
     path('reporter', views.AddReporter.as_view()),
     path('updateReporter/<id>', views.AddReporter.as_view()),
     path('article', views.AddArticle.as_view()),
]