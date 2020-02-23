from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate, login
from . import constants as user_constants
from apps.tution import selectors as tution_selectors
from . import services as user_services
from .validators import *
from .selectors import *
from .tokens import get_jwt_tokens_for_user
from .models import UserProfile, AllZipCode
from apps.mailers import utils as mailer_utils


class UserRegistrationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=64)
    confirm_password = serializers.CharField(max_length=64)
    user_type = serializers.ChoiceField(
        choices=[user_constants.STUDENT, user_constants.TUTOR])

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError(
                {'password': 'Passwords did not match'})
        return data

    def validate_email(self, val):
        if not isUniqueEmail(val):
            raise serializers.ValidationError(
                "Account with this email already exists")
        return val

    def create(self, validated_data):
        user = user_services.create_user(**validated_data)
        request = self.context.get('request')
        mailer_utils.send_account_activation_mail(request, user)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('name', 'email', 'phone')


class UserProfileGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('name', 'dob', 'gender', 'is_verified', 'created_at')


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=64, required=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        request = self.context.get('request')

        if isEmailVerificationPending(email):
            raise serializers.ValidationError(
                {"status": user_constants.ACCOUNT_INACTIVE})
        else:
            user = authenticate(request, email=email, password=password)
            data['user'] = user
            if user is not None:
                data['status'] = user_constants.ACCOUNT_ACTIVE
                tokens = get_jwt_tokens_for_user(user)
                data['access'] = tokens.get('access')
                data['refresh'] = tokens.get('refresh')
                login(request, user)
            else:
                raise serializers.ValidationError(
                    {'status': user_constants.ACCOUNT_DOESNOTEXIST})
        return data


class AccountActivationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, data):
        email = data.get('email')
        user = get_user(email=email)
        data['user'] = user
        request = self.context.get('request')
        if user is None:
            raise serializers.ValidationError(
                {'detail': 'No user associated with this email'})

        if not isEmailVerificationPending(email):
            raise serializers.ValidationError(
                {'detail': "No email verification pending for this email"})
        return data

    def send_activation_link(self):
        email = self.validated_data.get('email')
        request = self.context.get('request')
        user = self.validated_data.get('user')
        if user:
            mailer_utils.send_account_activation_mail(request, user)
        return user


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, data):
        email = data.get('email')
        user = get_user(email=email)
        data['user'] = user
        request = self.context.get('request')
        if user is None:
            raise serializers.ValidationError(
                {'detail': 'No user associated with this email'})
        else:
            if not user.is_active:
                raise serializers.ValidationError(
                    {'detail': 'Account not active for this email'})
        return data

    def send_password_link(self):
        email = self.validated_data.get('email')
        user = self.validated_data.get('user')
        request = self.context.get('request')
        if user:
            mailer_utils.send_password_reset_mail(request, user)
        return user


class SetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=64, required=True)
    confirm_password = serializers.CharField(max_length=64, required=True)

    def validate(self, data):
        email = data.get('email')
        user = get_user(email=email)
        data['user'] = user
        request = self.context.get('request')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if user is None:
            raise serializers.ValidationError(
                {'detail': 'No user associated with this email'})
        else:
            if not user.is_active:
                raise serializers.ValidationError(
                    {'detail': 'Account not active for this email'})

        if password != confirm_password:
            raise serializers.ValidationError(
                {'detail': 'Passwords did not match'})
        return data

    def change_password(self):
        user = self.validated_data.get('user')
        password = self.validated_data.get('password')
        user_services.change_user_password(user, password)
        return user


class UpdateProfileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        request = self.context.get('request')
        email = request.user.email
        users = user_services.update_profile(email, **validated_data)
        return users


class UpdatePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=64, required=True)
    new_password = serializers.CharField(max_length=64, required=True)
    confirm_new_password = serializers.CharField(max_length=64, required=True)

    def validate(self, data):
        old_password = data.get('old_password')
        new_password = data.get('new_password')
        confirm_new_password = data.get('confirm_new_password')
        request = self.context.get('request')
        user = authenticate(
            request, email=request.user.email, password=old_password)
        data['user'] = user
        if user is None:
            raise serializers.ValidationError(
                {'detail': "You provided a wrong current password"})
        if new_password != confirm_new_password:
            raise serializers.ValidationError(
                {'detail': 'New Passwords did not match'})
        return data

    def change_password(self):
        password = self.validated_data.get('new_password')
        user = self.validated_data.get('user')
        request = self.context.get('request')
        user = user_services.change_user_password(user, password)
        login(request, user)
        return user


class ZipCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllZipCode
        fields = '__all__'
