from .models import *
from . import constants as tution_constants
from apps.users import constants as user_constants
from apps.users import models as users_models
from django.db.models import Q


def get_category_groups():
    groups = Category.objects.filter(
        tag_type=tution_constants.GROUP, is_active=True).order_by('order')
    subject_categories = []
    for group in groups:
        childrens = CategoryRelation.objects.filter(
            parent=group, child__tag_type=tution_constants.TAG, child__is_active=True).order_by('order')
        subject_categories.append((group, childrens))

    return subject_categories


def get_categories():
    return Category.objects.filter(is_active=True)


def filtered_tution_data(**kwargs):
    location_keyword = kwargs.get('location_keyword')
    category = kwargs.get('category')
    experience = kwargs.get('experience')
    price_per_hour = kwargs.get('price_per_hour')
    qualification = kwargs.get('qualification')
    timing = kwargs.get('timing')
    gender = kwargs.get('gender')
    location_preferences = kwargs.get('location_preferences')

    # Required fields for minimum search functionality
    if category is None or location_keyword is None:
        raise Exception(
            "category and location_keyword are required keyword arguments")

    zipcode = None

    # Check whether the location_keyword is city or pincode
    try:
        isinstance(int(location_keyword), int)
        zipcode = str(location_keyword)
    except:
        zipcode = False

    # Gettings subject related users id
    valid_category_user_ids = users_models.UserCategory.objects.filter(
        Q(user__is_active=True) &
        Q(user__user_type=user_constants.TUTOR) &
        Q(category__name__icontains=category)
    ).values_list('user__id', flat=True)

    user_qs = users_models.UserProfile.objects.filter(
        user__is_active=True,
        user__user_type=user_constants.TUTOR,
        user__id__in=valid_category_user_ids
    )

    if zipcode == False:
        valid_zipcode_qs = users_models.AllZipcode.objects.filter(
            Q(po_name__icontains=location_keyword) |
            Q(district__icontains=location_keyword) |
            Q(state__icontains=location_keyword)
        ).first()
        if valid_category_user_ids is not None:
            user_qs = user_qs.filter(
                zipcode__icontains=valid_zipcode_qs.zipcode)
    else:
        user_qs = user_qs.filter(zipcode__icontains=zipcode)

    if location_preferences:
        valid_location_preferences_user_ids = users_models.UserLocationPreference.objects.filter(
            user__id__in=location_preferences).values_list('id', flat=True)

        if valid_location_preferences_user_ids:
            user_qs = user_qs.filter(
                user__id__in=valid_location_preferences_user_ids)

    if experience:
        user_qs = user_qs.filter(experience__lte=experience)

    if price_per_hour:
        user_qs = user_qs.filter(price_per_hour__lte=price_per_hour)

    if qualification:
        user_qs = user_qs.filter(qualification__icontains=qualification)

    if timing:
        user_qs = user_qs.filter(timing=timing)

    if gender:
        user_qs = user_qs.filter(gender=gender)

    return user_qs.values('user__id', 'user__user_type', 'gender', 'qualification', 'dob',
                          'price_per_hour', 'name', 'timing', 'experience', 'zipcode')


def is_valid_connection_request(tutor, student):
    return not TutionRequest.objects.filter(tutor=tutor, student=student).exists()


def get_connection_list(user):
    queryset = None
    user_type = user.user_type
    if user_type == user_constants.TUTOR:
        queryset = TutionRequest.objects.filter(tutor=user, is_active=True)
    if user_type == user_constants.STUDENT:
        queryset = TutionRequest.objects.filter(student=user, is_active=True)

    return queryset


def get_suggested_cities(location_keyword):
    try:
        isinstance(int(location_keyword), int)
        zipcode = str(location_keyword)
    except:
        zipcode = False

    if zipcode != False:
        data = users_models.AllZipCode.objects.filter(
            zipcode__icontains=int(zipcode))
    else:
        data = users_models.AllZipCode.objects.filter(
            Q(po_name__icontains=location_keyword) |
            Q(district__icontains=location_keyword) |
            Q(state__icontains=location_keyword))
    return data


def get_suggested_subjects(subject_keyword):
    subjects = Category.objects.filter(
        Q(name__icontains=subject_keyword) |
        Q(code__icontains=subject_keyword) |
        Q(tag_type=tution_constants.TAG) |
        Q(tag_type=tution_constants.SEARCH_TAG))

    return subjects
