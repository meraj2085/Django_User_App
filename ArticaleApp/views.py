from django.shortcuts import render
from .serializer import ArticleSerializer, ReporterSerializer
from .models import Reporter, Article
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["POST"])
def AddReporter(request):
    try:
        reporter = Reporter.objects.create(
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            email=request.data['email']
        )
        serializer = ReporterSerializer(reporter, many=False)
        return Response(serializer.data)
    except:
        message = {'message': 'Something went wrong'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def AddArticle(request):
    try:
        article = Article.objects.create(
            headline=request.data['headline'],
            reporter=request.data['reporter']
        )
        serializer = ArticleSerializer(Article, many=False)
        return Response(serializer.data)
    except:
        message = {'message': 'Something went wrong'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)