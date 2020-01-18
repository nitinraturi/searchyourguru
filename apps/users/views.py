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

    @action(detail=False, methods=['post'],url_name="register",url_path="register")
    def register(self,request):
        serializer = UserRegistrationSerializer(data=request.data)
        response = {}
        if serializer.is_valid():
            data = serializer.cleaned_data
            serializer.save()
            response['status'] = 'queued'
            # user = user_services.create_user(data,serializer=True)
            status_code = status.HTTP_201_CREATED
        else:
            data = serializer.errors
            response['errors'] = errors
            status_code = status.HTTP_400_BAD_REQUEST
        return Response({'data':data},status=status_code)
