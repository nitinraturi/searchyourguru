from django.contrib.auth import get_user_model
from django.db import transaction
from .models import *
from apps.tution.models import *


def create_user(**kwargs):
    User = get_user_model()
    data = {}
    name = kwargs.get('name')
    user_type = kwargs.get('user_type')
    email = kwargs.get('email')
    password = kwargs.get('password')
    user = User.objects.create_user(
        email, password, first_name=name, user_type=user_type)
    if user:
        kwargs.pop('user_type')
        create_or_update_user_profile(user, **kwargs)
    return user


def create_or_update_user_profile(user, **kwargs):
    with transaction.atomic():
        try:
            profile = UserProfile.objects.get(user=user)
            profile.name = user.first_name
            profile.email = user.email
            profile.phone = kwargs.get('phone')
            profile.zipcode = kwargs.get('zipcode')
            profile.experience = kwargs.get('experience')
            profile.price_per_hour = kwargs.get('price_per_hour')
            profile.qualification = kwargs.get('qualification')
            profile.timing = kwargs.get('timing')
            profile.dob = kwargs.get('dob')
            profile.gender = kwargs.get('gender')
            profile.experience = kwargs.get('experience')
            profile.save()
        except UserProfile.DoesNotExist:
            profile = UserProfile.objects.create(
                user=user, email=user.email, name=user.first_name, **kwargs)
        return profile


def update_profile(email, **kwargs):
    try:
        user_profile = UserProfile.objects.get(email=email)
        user_profile.name = kwargs.get('name')
        user_profile.user.first_name = kwargs.get('name')
        user_profile.save()
        user_profile.user.save()
        return user_profile
    except UserProfile.DoesNotExist:
        return None


def change_user_password(user, password):
    if not user:
        return None
    user.set_password(password)
    user.save()
    return user


def create_user_category(user, category_codes=None):
    if category_codes:
        ucs = [UserCategory(user=user, category=Category.objects.get(code=code))
               for code in category_codes]
        UserCategory.objects.bulk_create(ucs)


def create_user_location_preference(user, location_preferences=None):
    if location_preferences:
        lps = [UserLocationPreference(
            user=user, location_preference=lp) for lp in location_preferences]
        UserLocationPreference.objects.bulk_create(lps)


def insert_zipcodes_in_db(zipcodes, user_zipcode):
    objects = []
    for zipcode in zipcodes:
        obj = AllZipCode(po_name=zipcode.get('Name'), district=zipcode.get(
            'District'), state=zipcode.get('State'), country=zipcode.get('Country'), zipcode=zipcode.get('Pincode'))
        objects.append(obj)
    data = AllZipCode.objects.bulk_create(objects)
    return data
