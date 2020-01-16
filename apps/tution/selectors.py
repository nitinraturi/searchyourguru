from .models import *

def get_course():
    return Course.objects.all()

def get_subject():
    return Subject.objects.all()
