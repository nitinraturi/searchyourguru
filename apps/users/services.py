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
