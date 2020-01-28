from django.contrib.auth import get_user_model
from django.db import transaction
from .models import UserProfile

def create_user(**kwargs):
    User = get_user_model()
    data = {}
    name = kwargs.get('name')
    user_type = kwargs.get('user_type')
    email = kwargs.get('email')
    password = kwargs.get('password')
    user = User.objects.create_user(email,password,first_name=name,user_type=user_type)
    if user:
        kwargs.pop('user_type')
        create_or_update_user_profile(user,**kwargs)
    return user

def create_or_update_user_profile(user,**kwargs):
    with transaction.atomic():
        try:
            profile = UserProfile.objects.get(user=user)
            profile.name = user.first_name
            profile.email = user.email
            profile.phone = kwargs.get('phone')
            profile.save()
        except UserProfile.DoesNotExist:
            profile = UserProfile.objects.create(user=user,email=user.email,name=user.first_name,**kwargs)
        return profile

def update_profile(email,**kwargs):
    user_profile = UserProfile.objects.get(email=email)
    user_profile.name = kwargs.get('name')
    user_profile.user.first_name = kwargs.get('name')
    user_profile.save()
    user_profile.user.save()
    return user_profile

def change_user_password(user,password):
    user.set_password(password)
    user.save()
    return user
