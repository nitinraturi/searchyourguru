from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from . import constants as user_constants
from apps.tution import selectors as tution_selectors
from . import services as user_services

class UserRegistrationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=get_user_model().objects.all())])
    password = serializers.CharField(max_length=64)
    confirm_password = serializers.CharField(max_length=64)
    user_type = serializers.ChoiceField(choices=[user_constants.STUDENT,user_constants.TUTOR])

    def validate(self,data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError({'password':'Passwords did not match'})
        return data

    def create(self, validated_data):
        user = user_services.create_user(**validated_data)
        return user
