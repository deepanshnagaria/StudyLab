import os.path

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views import generic
from rest_framework.views import APIView
from rest_framework import generics,mixins
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, parsers, renderers, routers, serializers, viewsets, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from .serializers import PaperSerializer,TestPapersSerializer,TestSerializer
from rest_framework import viewsets, mixins, generics
from rest_framework.parsers import MultiPartParser, FormParser

from .paper_extractor import scrap_docx
from .models import *
from .serializers import PaperSerializer,TestPapersSerializer,FileSerializer

class QuestionsView(generics.ListCreateAPIView):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer

    def get(self,request,*args,**kwargs):
        qs = Paper.objects.all()
        serializer = PaperSerializer(qs,many=True)
        return Response(serializer.data)


class GetCurrentPathView(generic.ListView):

    def get(self,request,*args,**kwargs):
        path = request.get_full_path().rsplit('/', 1)[1]
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        location = BASE_DIR + '/media/images/' + path
        if(os.path.isfile(location)):
            f = open(location, "r")
            fileData = f.read()
            responseData = {
                    'path': path,
                    'content': fileData
                    }
            return JsonResponse(responseData)
        else:
            responseData = {
                    'path': path,
                    'content': 'Invalid request'
                    }
            return JsonResponse(responseData)

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

  def get(self,request,*args,**kwargs):
      qs = File.objects.all()
      serializer = FileSerializer(qs,many=True)
      return Response(serializer.data)

  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      filedata = file_serializer.data['file']
      BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
      filedata = os.path.join(BASE_DIR + filedata)
      (data, baseimg) = scrap_docx(filedata)
      for keys in baseimg.keys():
          with open(BASE_DIR + '/media/images/' +  keys,'w') as file:
              file.write(str(baseimg[keys]))
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestPaperView(generics.CreateAPIView):
    queryset = Paper.objects.all()
    serializer_class = TestPapersSerializer

class TestView(generics.ListCreateAPIView):
    queryset = Paper.objects.all()
    serializer_class = TestSerializer
