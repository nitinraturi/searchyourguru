from .models import *
from . import constants as tution_constants
from apps.users import models as users_models


def get_subjects():
    subjects = Category.objects.filter(tag_type=tution_constants.SUBJECT)
    subject_categories = []
    for subject in subjects:
        cr = CategoryRelation.objects.filter(
            parent=subject, child__tag_type=tution_constants.SUBJECT_CATEGORY)
        subject_categories.append((subject, cr))

    return subject_categories


def get_categories():
    return Category.objects.filter(is_active=True)


def filtered_tution_data(**kwargs):
    location_keyword = kwargs.get('location_keyword')
    user_type = kwargs.get('user_type')
    category = kwargs.get('category')
    experience = kwargs.get('experience')
    price_per_hour = kwargs.get('price_per_hour')
    qualification = kwargs.get('qualification')
    timing = kwargs.get('timing')
    gender = kwargs.get('gender')

    # Required fields for minimum search functionality
    if user_type is None or category is None or location_keyword is None:
        raise Exception(
            "user_type, category and location_keyword are required keyword arguments")

    zipcode = None

    # Check whether the location_keyword is city or pincode
    try:
        isinstance(int(location_keyword), int)
        zipcode = str(location_keyword)
    except:
        zipcode = False

    # Gettings subject related users id
    valid_category_user_ids = users_models.UserCategory.objects.filter(
        user__is_active=True,
        user__user_type=user_type,
        category__code=category
    ).values_list('user__id', flat=True)

    user_qs = users_models.UserProfile.objects.filter(
        user__is_active=True,
        user__user_type=kwargs.get('user_type'),
        user__id__in=valid_category_user_ids
    )

    if zipcode:
        user_qs = user_qs.filter(zipcode__icontains=zipcode)

    if experience:
        user_qs = user_qs.filter(experience=experience)

    if price_per_hour:
        user_qs = user_qs.filter(price_per_hour=price_per_hour)

    if qualification:
        user_qs = user_qs.filter(qualification__icontains=qualification)

    if timing:
        user_qs = user_qs.filter(timing=timing)

    if gender:
        user_qs = user_qs.filter(gender=gender)

    return user_qs.values('user__user_type', 'gender', 'qualification', 'dob',
                          'price_per_hour', 'name', 'timing', 'experience', 'zipcode')
