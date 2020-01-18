from .models import *
from django.contrib.auth import get_user_model

def create_user(**kwargs):
    User = get_user_model()
    user = User.objects.create_user(**kwargs)
    return user
