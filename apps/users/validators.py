from django.contrib.auth import get_user_model
from .models import UserProfile

def isUniqueEmail(email):
    User = get_user_model()
    return not User.objects.filter(email=email).exists()


def isEmailVerificationPending(email):
    User = get_user_model()
    return User.objects.filter(email=email,is_active=False).exists()

def isUserActive(email):
    User = get_user_model()
    return User.objects.filter(email=email,is_active=True).exists()


def isUniquePhone(phone):
    return not UserProfile.objects.filter(phone=phone).exists()
