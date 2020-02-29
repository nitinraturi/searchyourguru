from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from rest_framework import views, viewsets, status, renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model, logout
from .serializers import *
from . import services as user_services
from . import selectors as user_selectors
from .utils import *


class AuthViewSet(viewsets.ViewSet):
    queryset = get_user_model().objects.all()
    renderer_classes = [renderers.JSONRenderer]

    @action(detail=False, methods=['post'], url_name="register", url_path="auth/register")
    def account_register(self, request):
        serializer = UserRegistrationSerializer(
            data=request.data, context={"request": request})
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
        return Response(response, status=status_code)

    @action(detail=False, methods=['post'], url_name="login", url_path="auth/login")
    def account_login(self, request):
        response = {}
        serializer = LoginSerializer(
            data=request.data, context={"request": request})
        if serializer.is_valid():
            data = serializer.validated_data
            response['status'] = data.get('status')
            response['access'] = data.get('access')
            response['refresh'] = data.get('refresh')
            response['user_type'] = data.get('user').user_type
            status_code = status.HTTP_200_OK
        else:
            response = serializer.errors
            status_code = status.HTTP_403_FORBIDDEN
        return Response(response, status=status_code)

    @action(detail=False, methods=['post'], url_name="change_password", url_path="auth/change-password")
    def change_password(self, request):
        response = {}
        serializer = SetPasswordSerializer(
            data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.change_password()
            data = serializer.validated_data
            response['success'] = True
            status_code = status.HTTP_200_OK
        else:
            response = serializer.errors
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(response, status=status_code)

    @action(detail=False, methods=['post'], url_name="account_activation_link", url_path="auth/account-activation-link")
    def account_activation_link(self, request):
        response = {}
        serializer = AccountActivationSerializer(
            data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.send_activation_link()
            data = serializer.validated_data
            response['success'] = True
            status_code = status.HTTP_200_OK
        else:
            response = serializer.errors
            status_code = status.HTTP_403_FORBIDDEN
        return Response(response, status=status_code)

    @action(detail=False, methods=['post'], url_name="account_password_reset_link", url_path="auth/account-password-reset-link")
    def account_password_reset_link(self, request):
        response = {}
        serializer = PasswordResetSerializer(
            data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.send_password_link()
            data = serializer.validated_data
            response['success'] = True
            status_code = status.HTTP_200_OK
        else:
            response = serializer.errors
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(response, status=status_code)

    @action(detail=False, methods=['post'], url_name="logout", url_path="auth/logout")
    def account_logout(self, request):
        logout(request)
        return Response({'success': True}, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ViewSet):
    queryset = get_user_model().objects.all()

    @action(detail=False, methods=['get'], url_name="user_view", url_path="user", permission_classes=[IsAuthenticated])
    def user_view(self, request):
        response = {}
        user_profile = user_selectors.get_user_profile(request.user.email)
        serializer = UserProfileSerializer(user_profile)
        response = serializer.data
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

    @action(detail=False, methods=['post'], url_name="update_profile", url_path="user/update-profile", permission_classes=[IsAuthenticated])
    def update_profile(self, request):
        response = {}
        serializer = UpdateProfileSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            data = serializer.validated_data
            response['success'] = True
            status_code = status.HTTP_200_OK
        else:
            response = serializer.errors
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(response, status=status_code)

    @action(detail=False, methods=['post'], url_name="update_profile", url_path="user/update-password", permission_classes=[IsAuthenticated])
    def update_password(self, request):
        response = {}
        serializer = UpdatePasswordSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.change_password()
            response['success'] = True
            status_code = status.HTTP_200_OK
        else:
            response = serializer.errors
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(response, status=status_code)

    @action(detail=False, methods=['post'], url_name="zipcode_check", url_path="user/zipcode-check")
    def check_zipcode(self, request):
        db_zipcode = user_selectors.get_zipcode(request.data['zipcode'])
        if db_zipcode.count() == 0:
            api_zipcodes = fetch_zipcode_from_api(
                request.data['zipcode'])
            if api_zipcodes is None:
                return Response({
                    "Zipcode": "Invalid zipcode"
                }, status=status.HTTP_400_BAD_REQUEST)
            user_services.insert_zipcodes_in_db(
                api_zipcodes, request.data['zipcode'])
            db_zipcode = user_selectors.get_zipcode(request.data['zipcode'])
        serializer = ZipCodeSerializer(
            "https://www.clovia.com/active-wear/s/db_zipcode", many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_name="contact", url_path="contact")
    def contact(self, request):
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'ok': 1}, status=status.HTTP_200_OK)


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
        return render(request, 'account/activation.html', {'new_user': user, 'account_activated': True})
    else:
        return render(request, 'account/activation.html', {'new_user': user, 'account_activated': False})


def password_reset_verification(request, uidb64, token):
    from django.utils.encoding import force_text
    from django.utils.http import urlsafe_base64_decode
    from .tokens import password_reset_token

    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and password_reset_token.check_token(user, token):
        return render(request, 'account/password_reset.html', {'user': user, 'password_reset_verification': True})
    else:
        return render(request, 'account/password_reset.html', {'user': user, 'password_reset_verification': False})
