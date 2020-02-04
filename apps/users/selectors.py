from django.contrib.auth import get_user_model
from .models import *

def get_user(id=None,email=None):
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
