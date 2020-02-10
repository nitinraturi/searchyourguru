from rest_framework import serializers
from .models import *
from apps.users import constants as user_constants


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'code')


class CategoryRelationSerializer(serializers.ModelSerializer):
    child = CategorySerializer()

    class Meta:
        model = CategoryRelation
        fields = ('child',)


class SearchSerializer(serializers.Serializer):
    location_keyword = serializers.CharField(
        max_length=50)
    # zipcode = serializers.CharField(
    #     max_length=10, required=False, allow_null=True)
    # user_type = serializers.ChoiceField(
    #     choices=user_constants.USER_TYPE_CHOICES)
    category = serializers.CharField(max_length=50)
    experience = serializers.IntegerField(required=False, allow_null=True)
    price_per_hour = serializers.FloatField(required=False, allow_null=True)
    qualification = serializers.CharField(
        max_length=255, required=False, allow_null=True)
    location_preferences = serializers.ChoiceField(
        choices=user_constants.LOCATION_PREFERENCE, required=False, allow_null=True)
    timing = serializers.ChoiceField(
        choices=user_constants.TUTION_TIMINGS, required=False, allow_null=True)
    gender = serializers.ChoiceField(
        choices=user_constants.GENDER_CHOICES, required=False, allow_null=True)
