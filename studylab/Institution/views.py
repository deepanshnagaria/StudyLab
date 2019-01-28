from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CenterSerializer
from .models import *

class CenterView(APIView):

    def get(self, request):
        centers = Center.objects.all()
        serializer = CenterSerializer(centers, many=True)
        return Response({"centers": serializer.data})
