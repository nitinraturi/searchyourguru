from .models import *
from . import constants as tution_constants


def get_subjects():
    subjects = Category.objects.filter(tag_type=tution_constants.SUBJECT)
    subject_categories = []
    for subject in subjects:
        cr = CategoryRelation.objects.filter(
            parent=subject, child__tag_type=tution_constants.SUBJECT_CATEGORY)
        subject_categories.append((subject, cr))

    return subject_categories

def get_categories():
    return Category.objects.filter(is_active=True)