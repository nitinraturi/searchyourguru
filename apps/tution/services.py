from .models import *


def add_tution_connection(tutor, student):
    tution_request = TutionRequest.objects.create(
        tutor=tutor, student=student)

    return tution_request
