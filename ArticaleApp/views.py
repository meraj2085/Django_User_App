from django.shortcuts import render
from .serializer import ArticleSerializer, ReporterSerializer
from .models import Reporter, Article
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView

# Create your views here.
class AddReporter(GenericAPIView):
    serializer_class = ReporterSerializer
    @swagger_auto_schema(operation_summary="Add reporter",operation_description='Adding new reporter in the database') 
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


class AddArticle(GenericAPIView):
    serializer_class = ArticleSerializer
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
