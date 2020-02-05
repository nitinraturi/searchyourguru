from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from apps.users.managers import UserManager
from . import constants as user_constants


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, null=True, db_index=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    user_type = models.PositiveSmallIntegerField(
        choices=user_constants.USER_TYPE_CHOICES)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = UserManager()


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="user_profile")
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, db_index=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    experience = models.FloatField(null=True, blank=True)
    price_per_hour = models.FloatField(null=True, blank=True)
    qualification = models.CharField(max_length=255, blank=True, null=True)
    timing = models.PositiveSmallIntegerField(
        choices=user_constants.TUTION_TIMINGS, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(
        choices=user_constants.GENDER_CHOICES, null=True, blank=True)
    experience = models.FloatField(default=0.0)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


class UserCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('tution.Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category.name

    class Meta:
        unique_together = ['user', 'category']


class UserLocationPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location_preference = models.PositiveSmallIntegerField(
        choices=user_constants.LOCATION_PREFERENCE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        unique_together = ['user', 'location_preference']
