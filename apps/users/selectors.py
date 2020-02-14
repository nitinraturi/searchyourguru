from django.contrib.auth import get_user_model
from .models import *
import requests


def get_user(id=None, email=None):
    User = get_user_model()
    if id is None and email is None:
        raise Exception("Either id or email is required to retrieve user")
    user = None
    try:
        if id:
            user = User.objects.get(id=id)
        if email:
            user = User.objects.get(email=email)
    except User.DoesNotExist:
        pass
    return user


def get_user_profile(email):
    try:
        return UserProfile.objects.get(email=email)
    except UserProfile.DoesNotExist:
        return None


def get_zipcode(zipcode):
    try:
        return AllZipCode.objects.get(zipcode=zipcode)
    except AllZipCode.DoesNotExist:
        return None


def fetch_zipcode_from_api(zipcode):
    zipcode_api_endpoint = f"https://api.postalpincode.in/pincode/{zipcode}"
    response = requests.get(zipcode_api_endpoint)
    print(response.status_code)
    print(response.headers['content-type'])
    print(response.encoding)
    print(response.text)
    print(response.json())






