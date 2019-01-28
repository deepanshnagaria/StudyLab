# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Institution
from .serializers import InstitutionSerializer

class InstitutionView(APIView):
    def get(self, request):
        institutions = Institution.objects.all()
        serializer = InstitutionSerializer(institutions, many=True)
        return Response({"institutions": serializer.data})

    # def post(self, request):
    #     Institution = request.data.get('Institution')

    #     serializer = InstitutionSerializer(data=Institution)
    #     if serializer.is_valid(raise_exception=True):
    #         Institution_saved = serializer.save()
    #     return Response({"success": "Institution '{}' created successfully".format(Institution_saved.name)})

