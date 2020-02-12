from rest_framework import serializers
from .models import *
from apps.users import constants as user_constants
from . import selectors as tution_selectors


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


class TutionRequestSerializer(serializers.Serializer):
    from_user_id = serializers.IntegerField()
    to_user_id = serializers.IntegerField()

    def validate(self, data):
        from_user_id = data.get('from_user_id')
        to_user_id = data.get('to_user_id')

        is_valid_req = tution_selectors.is_valid_connection_request(
            from_user_id, to_user_id)

        if not is_valid_req:
            raise serializers.ValidationError(
                {'detail': 'Either you are already connected or your previous request is not accepted yet'})

        return data
