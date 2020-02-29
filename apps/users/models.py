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
    experience = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(
        choices=user_constants.GENDER_CHOICES, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


class AllZipCode(models.Model):
    zipcode = models.CharField(
        db_index=True, max_length=10, blank=True, null=True)
    po_name = models.CharField(
        db_index=True, max_length=255, null=True, blank=True)
    district = models.CharField(
        db_index=True, max_length=255, null=True, blank=True)
    country = models.CharField(
        db_index=True, max_length=255, null=True, blank=True)
    state = models.CharField(
        db_index=True, max_length=255, null=True, blank=True)
    latitude = models.FloatField(db_index=True, null=True, blank=True)
    longitude = models.FloatField(db_index=True, null=True, blank=True)
    city = models.CharField(
        db_index=True, max_length=255, blank=True, null=True)

    def __str__(self):
        return self.zipcode

    class Meta:
        verbose_name_plural = 'All ZipCodes'


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email