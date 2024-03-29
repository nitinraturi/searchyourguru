from rest_framework import serializers
from .models import *
from apps.users import constants as user_constants
from apps.users import selectors as user_selectors
from . import selectors as tution_selectors
from apps.users import serializers as users_serializers
from apps.tution import services as tution_services


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
    tutor = users_serializers.UserGuestSerializer()
    category = CategorySerializer()
    applications = serializers.SerializerMethodField('get_applications')
    created_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        return obj.updated_at.strftime("%Y-%m-%d")

    class Meta:
        model = Tution
        fields = '__all__'

    def get_applications(self, obj):
        queryset = tution_selectors.tution_application_received(
            obj.tutor, obj.id)
        data = TutionApplicantSerializer(queryset, many=True)
        return data.data


class TutionCreateSerializer(serializers.ModelSerializer):
    category = serializers.CharField(max_length=255)

    class Meta:
        model = Tution
        fields = '__all__'

    def validate(self, data):
        request = self.context.get('request')
        category = tution_selectors.get_category(data.get('category'))
        if request.user.user_type not in [user_constants.TUTOR, user_constants.SUPERUSER]:
            raise serializers.ValidationError({'detail': 'Not a valid tutor'})

        if not category:
            raise serializers.ValidationError(
                {'detail': 'Not a valid category'})
        else:
            data['category'] = category
        return data


class TutionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tution
        fields = ('title', 'price', 'description',
                  'timing', 'location', 'is_active')

    def validate(self, data):
        request = self.context.get('request')
        tution = self.context.get('tution')
        if tution is None:
            raise serializers.ValidationError({'detail': 'Invalid tution'})
        elif request.user.id != tution.tutor.id:
            raise serializers.ValidationError({'detail': 'Not a valid tutor'})
        return data


class TutionDeleteSerializer(serializers.Serializer):
    tution_id = serializers.IntegerField()

    def validate(self, data):
        request = self.context.get('request')
        tution_id = data.get('tution_id')
        print("asdasd", tution_id)
        tution = tution_selectors.get_tution(tution_id)
        if tution is None:
            raise serializers.ValidationError({'detail': 'Invalid tution'})
        elif request.user.id != tution.tutor.id:
            raise serializers.ValidationError({'detail': 'Not a valid tutor'})
        data['tution'] = tution
        return data

    def delete_tution(self):
        tution = self.validated_data.get('tution')
        tution_services.delete_tution(tution)


class TutionRequestSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(min_length=10, max_length=10)

    class Meta:
        model = TutionRequest
        fields = ('tution', 'phone', 'address',)
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
                {'detail': 'Request already sent, please wait for tutor acceptance. You can check your dashboard for tution status updates'})

        return data


class TutionAppliedSerializer(serializers.ModelSerializer):
    tution = TutionListSerializer()
    student = users_serializers.UserGuestSerializer()
    updated_at = serializers.SerializerMethodField()

    def get_updated_at(self, obj):
        return obj.updated_at.strftime("%Y-%m-%d")

    class Meta:
        model = TutionRequest
        fields = '__all__'


class TutionApplicantSerializer(serializers.ModelSerializer):
    student = users_serializers.UserGuestSerializer()

    class Meta:
        model = TutionRequest
        fields = '__all__'
