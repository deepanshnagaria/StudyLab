from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics,mixins,permissions

from .serializers import CenterSerializer
from .models import *

class CenterView(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        generics.ListAPIView):

    serializer_class = CenterSerializer
    queryset = Center.objects.all()
    def get(self, request):
        centerData = Center.objects.all()
        serializer = CenterSerializer(centerData, many=True)
        return Response(serializer.data)

    def post(self, request,*args, **kwargs):
        return self.create(request,*args,**kwargs)
