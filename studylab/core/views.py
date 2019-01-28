# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics,mixins,permissions
from rest_framework.views import APIView
from .models import Institution, Subjects
from rest_framework.permissions import IsAuthenticated

from .serializers import InstitutionSerializer, SubjectsSerializer

class InstitutionView(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        generics.ListAPIView):

    serializer_class = InstitutionSerializer
    def get(self, request):
        institutions = Institution.objects.all()
        serializer = InstitutionSerializer(institutions, many=True)
        return Response(serializer.data)

    def post(self, request,*args, **kwargs):
        # data1 = request.data
        # print(data1)
        # serializer = InstitutionSerializer(data1)
        # if serializer.is_valid(data=data1):
        #     Institution_saved = serializer.save()
        # return Response({"success": "Institution '{}' created successfully".format(Institution_saved.name)})
        return self.create(request,*args,**kwargs)


class SubjectsView(APIView):

    def get(self, request):
        subjects = Subjects.objects.all()
        serializer = SubjectsSerializer(subjects, many=True)
        return Response({"subjects": serializer.data})

    # def post(self, request):
    #     # Institution = request.data.get('Institution')

    #     serializer = InstitutionSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         Institution_saved = serializer.save()
    #     return Response({"success": "Institution '{}' created successfully".format(Institution_saved.name)})

