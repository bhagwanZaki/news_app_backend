from typing import NoReturn
from django.shortcuts import render
from .models import News
from rest_framework import serializers, viewsets,permissions,status  
from rest_framework.views import APIView
from .serializers import newsSerializers
from rest_framework.response import Response

class newsAdminApi(viewsets.ModelViewSet):
    serializer_class = newsSerializers
    permissions_classes = [
        permissions.IsAdminUser
    ]
    queryset = News.objects.all()

class newsApi(APIView):
    permissions_classes = [permissions.AllowAny]

    def get(self,request,format=None):
        news = News.objects.all()
        try:
            if len(news) > 3:
                data = news[3:]
            else:
                data = news
            data.reverse()
            serializer = newsSerializers(data,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response([],status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class latestNewsApi(APIView):
    permissions_classes = [permissions.AllowAny]

    def get(self,request,format=None):
        news = News.objects.all()
        try:
            if len(news) > 3:
                data = news[:3]
            else:
                data = news
            data.reverse()
            serializer = newsSerializers(data,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response([],status=status.HTTP_500_INTERNAL_SERVER_ERROR)
