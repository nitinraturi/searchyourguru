from .models import *


def delete_tution(tution):
    tution.is_deleted = True
    tution.is_active = False
    tution.save()
