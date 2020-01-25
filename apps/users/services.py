from django.contrib.auth import get_user_model
from .models import *

def create_user(**kwargs):
    User = get_user_model()
    data = {}
    data['first_name'] = kwargs.get('name')
    data['user_type'] = kwargs.get('user_type')
    data['phone'] = kwargs.get('phone')
    email = kwargs.get('email')
    password = kwargs.get('password')
    user = User.objects.create_user(email,password,**data)
    return user

def update_profile(email,**kwargs):
    User = get_user_model()
    data = {}
    data['first_name'] = kwargs.get('name')
    return User.objects.filter(email=email).update(**data)

def change_user_password(user,password):
    user.set_password(password)
    user.save()
    return user
