from rest_framework import serializers
from .models import *
from apps.users import constants as user_constants
from apps.users import selectors as user_selectors
from . import selectors as tution_selectors
from apps.users import serializers as users_serializers


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


class ConnectionAddSerializer(serializers.Serializer):
    tutor_id = serializers.IntegerField()
    student_id = serializers.IntegerField()

    def validate(self, data):
        tutor_id = data.get('tutor_id')
        student_id = data.get('student_id')

        tutor = user_selectors.get_user(id=tutor_id)
        student = user_selectors.get_user(id=student_id)
        data['tutor'] = tutor
        data['student'] = student

        if tutor is None:
            raise serializers.ValidationError({'detail': 'No such user'})
        elif tutor.user_type not in [user_constants.TUTOR, user_constants.SUPERUSER]:
            raise serializers.ValidationError({'detail': 'Not a valid tutor'})
        elif student.user_type not in [user_constants.STUDENT, user_constants.SUPERUSER]:
            raise serializers.ValidationError(
                {'detail': 'Not a valid student'})
        else:
            is_valid_req = tution_selectors.is_valid_connection_request(
                tutor, student)

        if not is_valid_req:
            raise serializers.ValidationError(
                {'detail': 'Either you are already connected or your previous request is not accepted yet'})

        return data


class TutionRequestSerializer(serializers.ModelSerializer):
    student = users_serializers.UserProfileSerializer()

    class Meta:
        model = TutionRequest
        fields = ('id', 'student', 'is_accepted', 'created_at')


class ConnectionAcceptSerializer(serializers.Serializer):
    tution_id = serializers.IntegerField()

    def validate(self, data):
        request = self.context.get('request')
        if request.user.user_type not in [user_constants.TUTOR, user_constants.SUPERUSER]:
            raise serializers.ValidationError({'detail': 'Not a valid tutor'})
        return data
