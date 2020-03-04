from .models import *
from . import constants as tution_constants
from apps.users import constants as user_constants
from apps.users import models as users_models
from django.db.models import Q
from django.core.cache import cache


def get_categories():
    return Category.objects.filter(is_active=True)


def get_category(code):
    try:
        return Category.objects.get(code=code)
    except Category.DoesNotExist:
        pass


def filtered_tution_data(**kwargs):
    location_keyword = kwargs.get('location_keyword')
    category = kwargs.get('category')
    experience = kwargs.get('experience')
    price_per_hour = kwargs.get('price_per_hour')
    timing = kwargs.get('timing')
    gender = kwargs.get('gender')
    location_preferences = kwargs.get('location_preferences')

    # Required fields for minimum search functionality
    if category is None or location_keyword is None:
        raise Exception(
            "category and location_keyword are required keyword arguments")

    # Check whether the location_keyword is city or pincode
    try:
        zipcode = int(location_keyword)
    except:
        zipcode = None

    tutions = Tution.objects.filter(
        Q(category__name__icontains=category),
        Q(category__code__icontains=category),
        tutor__is_active=True,
        is_deleted=False
    )
    print("tutions", tutions)
    if zipcode:
        zipcode = users_models.AllZipCode.objects.filter(zipcode__search=zipcode
                                                         ).values_list('po_name', flat=True)
        tutions = tutions.filter(
            Q(area__icontains=location_keyword) |
            Q(area__in=zipcode))
    else:
        tutions = tutions.filter(area__search=location_keyword)

    if price_per_hour:
        tutions = tutions.filter(price__lte=price_per_hour)

    if timing:
        tutions = tutions.filter(timing=timing)

    if gender:
        tutions = tutions.filter(tutor__user_profile__gender=gender)

    if experience:
        tutions = tutions.filter(
            tutor__user_profile__experience__lte=experience)

    if location_preferences:
        tutions = tutions.filter(location__in=location_preferences)

    return tutions


def get_suggested_cities(location_keyword):
    cache_key = "location_"+location_keyword.replace(" ", "_")
    data = cache.get(cache_key)
    if data is None:
        try:
            isinstance(int(location_keyword), int)
            zipcode = str(location_keyword)
        except:
            zipcode = False

        if zipcode != False:
            zipcode = int(zipcode)
            data = users_models.AllZipCode.objects.filter(
                Q(zipcode__search=zipcode) |
                Q(zipcode__istartswith=zipcode)
            )
        else:
            data = users_models.AllZipCode.objects.filter(
                Q(po_name__search=location_keyword) |
                Q(district__search=location_keyword) |
                Q(city__search=location_keyword) |
                Q(po_name__istartswith=location_keyword) |
                Q(district__istartswith=location_keyword) |
                # Q(country__istartswith=location_keyword) |
                # Q(state__istartswith=location_keyword) |
                Q(city__istartswith=location_keyword)
            )
        data = data.distinct('po_name')[:20]
        cache.set(cache_key, data, 86400 * 365)
    else:
        pass
    return data


def get_suggested_subjects(subject_keyword):
    subjects = Category.objects.filter(
        Q(name__search=subject_keyword) |
        Q(code__search=subject_keyword) |
        Q(name__icontains=subject_keyword) |
        Q(code__icontains=subject_keyword) |
        Q(tag_type=tution_constants.TAG) |
        Q(tag_type=tution_constants.SEARCH_TAG)
    )

    return subjects


def get_tutions(user):
    return Tution.objects.filter(tutor=user, is_deleted=False)


def get_tution(id):
    try:
        return Tution.objects.get(id=id)
    except Tution.DoesNotExist:
        pass


def tution_request_exists(tution_id, student):
    return TutionRequest.objects.filter(tution__id=tution_id, student=student).exists()


def tution_applied_requests(user):
    return TutionRequest.objects.filter(student=user)


def tution_application_received(tutor, tution_id):
    return TutionRequest.objects.filter(tution__tutor=tutor, tution__id=tution_id)
