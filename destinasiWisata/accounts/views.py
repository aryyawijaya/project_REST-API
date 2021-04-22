from django.shortcuts import render
from accounts.serializers import *
from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from knox.models import AuthToken
from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView, LogoutView
from rest_framework.views import APIView
from django.http import Http404

# POST register/
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                'status': status.HTTP_201_CREATED,
                'message': 'success create new user',
                'user': UserSerializer(user, context=self.get_serializer_context()).data,
                'token': AuthToken.objects.create(user)[1]
            }
        )

# POST login/
class LoginAPI(LoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class LogoutAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        logout(request)
        request._auth.delete() # delete token
        return Response(
            {
                'status': status.HTTP_200_OK,
                'message': 'success logged out'
            }
        )

# GET user/
class UserList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(
            {
                'status': status.HTTP_200_OK,
                'message': 'success get users',
                'data': serializer.data
            }
        )

# GET user/id/
class UserDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    # GET
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(
            {
                'status': status.HTTP_200_OK,
                'message': 'success get user',
                'data': serializer.data
            }
        )