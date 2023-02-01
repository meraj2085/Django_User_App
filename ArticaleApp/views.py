from django.shortcuts import render
from .serializer import ArticleSerializer, ReporterSerializer
from .models import Reporter, Article
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.
class AddReporter(APIView):
    def post(self, request):
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


class AddArticle(APIView):
    def post(self, request):
        try:
            article = Article.objects.create(
                headline=request.data['headline'],
                reporter_id=request.data['reporter_id']
            )
            serializer = ArticleSerializer(article, many=False)
            return Response(serializer.data)
        except:
            message = {'message': 'Something went wrong'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
