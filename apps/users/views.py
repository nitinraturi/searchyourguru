from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from rest_framework import views, viewsets, status, renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model,logout
from .serializers import *
from . import services as user_services

class AuthViewSet(viewsets.ViewSet):
    queryset = get_user_model().objects.all()
    renderer_classes = [renderers.JSONRenderer]

    @action(detail=False, methods=['post'],url_name="register",url_path="auth/register")
    def account_register(self,request):
        serializer = UserRegistrationSerializer(data=request.data,context={"request":request})
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

    @action(detail=False, methods=['post'],url_name="login",url_path="auth/login")
    def account_login(self,request):
        response = {}
        serializer = LoginSerializer(data=request.data,context={"request":request})
        if serializer.is_valid():
            data = serializer.validated_data
            response['status'] = data.get('status')
            status_code = status.HTTP_200_OK
        else:
            response = serializer.errors
            status_code = status.HTTP_403_FORBIDDEN
        return Response(response,status=status_code)

    @action(detail=False, methods=['post'],url_name="account_activation_link",url_path="auth/account-activation-link")
    def account_activation_link(self,request):
        response = {}
        serializer = AccountActivationSerializer(data=request.data,context={"request":request})
        if serializer.is_valid():
            serializer.send_activation_link()
            data = serializer.validated_data
            response['success'] = True
            status_code = status.HTTP_200_OK
        else:
            response = serializer.errors
            status_code = status.HTTP_403_FORBIDDEN
        return Response(response,status=status_code)

    @action(detail=False, methods=['post'],url_name="logout",url_path="auth/logout")
    def account_logout(self,request):
        logout(request)
        return Response({'success':True},status=status.HTTP_200_OK)


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


def activate_account(request, uidb64, token):
    from django.utils.encoding import force_text
    from django.utils.http import urlsafe_base64_decode
    from .tokens import account_activation_token

    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request,'account/login.html',{'new_user':user,'account_activated':True})
    else:
        return render(request,'account/login.html',{'new_user':user,'account_activated':False})
