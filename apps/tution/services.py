from .models import *


def get_tutions(user):
    return Tution.objects.filter(is_active=True, tutor=user)
