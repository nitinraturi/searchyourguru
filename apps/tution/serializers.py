from rest_framework import serializers
from .models import *
from apps.users import constants as user_constants
from apps.users import selectors as user_selectors
from . import selectors as tution_selectors
from apps.users import serializers as users_serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'code')


class CategoryRelationSerializer(serializers.ModelSerializer):
    child = CategorySerializer()

    class Meta:
        model = CategoryRelation
        fields = ('child',)


class SearchSerializer(serializers.Serializer):
    location_keyword = serializers.CharField(
        max_length=50)
    category = serializers.CharField(max_length=50)
    experience = serializers.IntegerField(required=False, allow_null=True)
    price_per_hour = serializers.FloatField(required=False, allow_null=True)
    location_preferences = serializers.ListField(
        child=serializers.ChoiceField(
            choices=tution_constants.LOCATION_PREFERENCE), required=False, allow_null=True
    )
    timing = serializers.ChoiceField(
        choices=tution_constants.TUTION_TIMINGS, required=False, allow_null=True)
    gender = serializers.ChoiceField(
        choices=user_constants.GENDER_CHOICES, required=False, allow_null=True)


class CitySuggestionSerializer(serializers.Serializer):
    location_keyword = serializers.CharField(
        max_length=50)


class SubjectSuggestionSerializer(serializers.Serializer):
    subject_keyword = serializers.CharField(
        max_length=50)


class TutionListSerializer(serializers.ModelSerializer):
    tutor = users_serializers.UserProfileGuestSerializer()
    category = CategorySerializer()

    class Meta:
        model = Tution
        fields = '__all__'


class TutionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tution
        fields = '__all__'

    def validate(self, data):
        request = self.context.get('request')
        if request.user.user_type not in [user_constants.TUTOR, user_constants.SUPERUSER]:
            raise serializers.ValidationError({'detail': 'Not a valid tutor'})
        return data


class TutionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutionRequest
        fields = ('tution',)
        read_only_fields = ('student',)

    def validate(self, data):
        request = self.context.get('request')
        tution = data.get('tution')

        if request.user.user_type not in [user_constants.STUDENT, user_constants.SUPERUSER]:
            raise serializers.ValidationError({
                'detail': 'You are not authorized'
            })

        if tution_selectors.tution_request_exists(tution.id, request.user):
            raise serializers.ValidationError(
                {'detail': 'Request already sent, please wait for tutor acceptance'})

        return data
