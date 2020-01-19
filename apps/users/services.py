from django.contrib.auth import get_user_model
from .models import *

def create_user(**kwargs):
    User = get_user_model()
    data = {}
    data['first_name'] = kwargs.get('name')
    data['user_type'] = kwargs.get('user_type')
    email = kwargs.get('email')
    password = kwargs.get('password')
    user = User.objects.create_user(email,password,**data)
    return user

def get_user(id=None,email=None):
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
