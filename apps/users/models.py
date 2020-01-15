from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from apps.users.managers import UserManager
from . import constants as user_constants
from apps.tution.models import Course, Subject

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, null=True, db_index=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    user_type = models.PositiveSmallIntegerField(choices=user_constants.USER_TYPE_CHOICES)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = UserManager()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name="user_profile")
    phone = models.CharField(max_length=255,blank=True,null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
