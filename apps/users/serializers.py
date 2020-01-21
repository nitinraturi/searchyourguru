from rest_framework import serializers
from django.contrib.auth import get_user_model,authenticate, login
from . import constants as user_constants
from apps.tution import selectors as tution_selectors
from . import services as user_services
from .validators import *

class UserRegistrationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=10)
    password = serializers.CharField(max_length=64)
    confirm_password = serializers.CharField(max_length=64)
    user_type = serializers.ChoiceField(choices=[user_constants.STUDENT,user_constants.TUTOR])

    def validate(self,data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError({'password':'Passwords did not match'})
        return data

    def validate_email(self,val):
        if not isUniqueEmail(val):
            raise serializers.ValidationError("Account with this email already exists")
        return val

    def validate_phone(self,val):
        if not isUniquePhone(val):
            raise serializers.ValidationError("Account with this phone already exists")
        return val

    def create(self, validated_data):
        user = user_services.create_user(**validated_data)
        request = self.context.get('request')
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('first_name','email','user_type')

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=64,required=True)

    def validate(self,data):
        email = data.get("email")
        password = data.get("password")
        request = self.context.get('request')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
        else:
            raise serializers.ValidationError({'detail':'No active account found with the given credentials'})
        return data
