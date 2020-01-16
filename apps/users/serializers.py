from rest_framework import serializers
from django.contrib.auth import get_user_model
from . import constants as user_constants
from apps.tution import selectors as tution_selectors

class UserRegistrationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=64)
    confirm_password = serializers.CharField(max_length=64)
    # course = serializers.MultipleChoiceField(choices=user_c)
    user_type = serializers.ChoiceField(choices=user_constants.USER_TYPE_CHOICES)

    def validate(self,data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError('Passwords did not match')
        return data
