from rest_framework.response import Response
from rest_framework import generics,mixins,permissions
from rest_framework.views import APIView
from .models import Institution, Subjects, Phase
from rest_framework.permissions import IsAuthenticated

from .serializers import InstitutionSerializer, SubjectsSerializer, PhaseSerializer

class InstitutionView(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        generics.ListAPIView):

    serializer_class = InstitutionSerializer
    def get(self, request):
        institutions = Institution.objects.all()
        serializer = InstitutionSerializer(institutions, many=True)
        return Response(serializer.data)

    def post(self, request,*args, **kwargs):
        return self.create(request,*args,**kwargs)

class SubjectsView(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        generics.ListAPIView):

    serializer_class = SubjectsSerializer
    def get(self, request):
        subjects = Subjects.objects.all()
        serializer = SubjectsSerializer(subjects, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PhaseView(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        generics.ListAPIView):

    serializer_class = PhaseSerializer
    def get(self, request):
        phaseData = Phase.objects.all()
        serializer = PhaseSerializer(phaseData, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, *kwargs)
