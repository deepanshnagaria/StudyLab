from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics,mixins
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, parsers, renderers, routers, serializers, viewsets, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from .serializers import PaperSerializer,TestPapersSerializer
from .models import *

class QuestionsView(mixins.CreateModelMixin,
                generics.ListAPIView):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer

    def get(self,request,*args,**kwargs):
        qs = Paper.objects.all()
        serializer = PaperSerializer(qs,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    


class TestPaperView(generics.CreateAPIView):
    queryset = Paper.objects.all()
    serializer_class = TestPapersSerializer
