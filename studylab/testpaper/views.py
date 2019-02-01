from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics,mixins
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, parsers, renderers, routers, serializers, viewsets, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from .serializers import PaperSerializer,TestPapersSerializer,TestSerializer
from .models import *
from rest_framework import viewsets
from .serializers import PaperSerializer,TestPapersSerializer,FileSerializer
from .models import *
from rest_framework.parsers import MultiPartParser, FormParser


class QuestionsView(generics.ListCreateAPIView):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer

    def get(self,request,*args,**kwargs):
        qs = Paper.objects.all()
        serializer = PaperSerializer(qs,many=True)
        return Response(serializer.data)

# class QuestionsViewSet(viewsets.ModelViewSet):
#     queryset = Paper.objects.all()
#     serializer_class = PaperSerializer

    # def retrieve(self,request,*args,**kwargs):
    #     obj = self.get_object()
    #     serializer = PaperSerializer(obj)
    #     # return HttpResponseNotAllowed('not allowed')
    #     return Response(serializer.data)

    # def list(self,request,*args,**kwargs):
    #     queryset = Paper.objects.all()
    #     # questions = self.get_queryset()
    #     serializer = PaperSerializer(queryset,many=True)
    #     return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    
class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestPaperView(generics.CreateAPIView):
    queryset = Paper.objects.all()
    serializer_class = TestPapersSerializer

class TestView(generics.ListCreateAPIView):
    queryset = Paper.objects.all()
    serializer_class = TestSerializer