from django.shortcuts import render
from .serializer import ArticleSerializer, ReporterSerializer
from .models import Reporter, Article
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
import jwt

# Create your views here.
class AddReporter(GenericAPIView):
    serializer_class = ReporterSerializer
    @swagger_auto_schema(operation_summary="Add reporter",operation_description='Adding new reporter in the database') 
    def post(self, request):
            serializer = ReporterSerializer(data=request.data)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'message': "Something went wrong", "status": status.HTTP_400_BAD_REQUEST, "errors": serializer.errors})

            serializer.save()
            encoded_jwt = jwt.encode({"email": request.data['email']}, "1a2b3c4d5e6f", algorithm="HS256")
            return Response({"token": encoded_jwt})
    

    def put(self, request, id):
        try:
            reporterObj = Reporter.get(id=id)
            serializer = ReporterSerializer(reporterObj, data=request.data)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'message': "Something went wrong", "status": status.HTTP_400_BAD_REQUEST, "errors": serializer.errors})

            serializer.save()
            encoded_jwt = jwt.encode({"email": request.data['email']}, "1a2b3c4d5e6f", algorithm="HS256")
            return Response({"token": encoded_jwt})
        except Exception as e:
            return Response({'message': "Invalid id", "status": status.HTTP_400_BAD_REQUEST})





class AddArticle(GenericAPIView):
    serializer_class = ArticleSerializer
    @swagger_auto_schema(operation_summary="Add article",operation_description='Adding new article in the Database')
    def post(self, request):
        try:
            article = Article.objects.create(
                headline=request.data['headline'],
                reporter_id=request.data['reporter']
            )
            serializer = ArticleSerializer(article, many=False)
            return Response(serializer.data)
        except:
            message = {'message': 'Something went wrong'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
