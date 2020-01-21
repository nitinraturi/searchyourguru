from django.contrib.auth import get_user_model

def isUniqueEmail(email):
    User = get_user_model()
    return not User.objects.filter(email=email).exists()

def isUniquePhone(phone):
    User = get_user_model()
    return not User.objects.filter(phone=phone).exists()
