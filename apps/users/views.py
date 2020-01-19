from django.shortcuts import render
from rest_framework import views, viewsets, status, renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import *
from . import services as user_services

class AuthViewSet(viewsets.ViewSet):
    queryset = get_user_model().objects.all()
    renderer_classes = [renderers.JSONRenderer]

    @action(detail=False, methods=['post'],url_name="register",url_path="auth/register")
    def register(self,request):
        serializer = UserRegistrationSerializer(data=request.data)
        response = {}
        if serializer.is_valid():
            data = serializer.validated_data
            serializer.save()
            response['status'] = 'queued'
            response['email'] = data.get('email')
            response['user_type'] = data.get('user_type')
            status_code = status.HTTP_201_CREATED
        else:
            response['status'] = 'failed'
            response['errors'] = serializer.errors
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(response,status=status_code)

    # @action(detail=False, methods=['post'],url_name="login",url_path="login")
    # def login(self,request):
    #

class UserViewSet(viewsets.ViewSet):
    queryset = get_user_model().objects.all()

    @action(detail=True,methods=['get'],url_name="user_view",url_path="user")
    def user_view(self,request,pk):
        response = {}
        user = user_services.get_user(id=pk)
        if user:
            serializer = UserSerializer(user)
            response = serializer.data
            status_code = status.HTTP_200_OK
        else:
            response['error'] = "User does not exist"
            status_code = status.HTTP_404_NOT_FOUND
        return Response(response,status=status_code)
