from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, parsers, renderers, routers, serializers, viewsets, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token

from .serializers import CreateSerializer, AuthTokenSerializer, userSerializer

class NewUser(APIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = CreateSerializer

    @staticmethod
    def post(request):
        serializer = CreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)
            user.save()

            token, created = Token.objects.get_or_create(user=user)
            logout(request)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            data = serializer.data
            data['token'] = token.key
            return Response(data, status=status.HTTP_200_OK)
        errors = serializer.errors
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    """
    A view that allows users to login providing their email and password.
    """
    authentication_classes = []
    permission_classes = []
    parser_classes = (parsers.JSONParser, parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        user_data = userSerializer(user, context={'request': request}).data
        user_data['token'] = token.key
        return Response(user_data, status=status.HTTP_202_ACCEPTED)

class Logout(APIView):
    @staticmethod
    def get(request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)
