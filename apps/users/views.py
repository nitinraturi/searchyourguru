from django.shortcuts import render
from rest_framework import views, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import *

class AuthViewSet(viewsets.ViewSet):
    queryset = get_user_model().objects.all()

    @action(detail=False, methods=['post'],url_name="register",url_path="register")
    def register(self,request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
        else:
            data = serializer.errors
        return Response({'data':data})
