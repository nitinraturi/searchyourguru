from .models import *


def add_tution_connection(tutor, student):
    tution_request = TutionRequest.objects.create(
        tutor=tutor, student=student)

    return tution_request


def get_tutions(user):
    return Tution.objects.filter(is_active=True, tutor=user)
