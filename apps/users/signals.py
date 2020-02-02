from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, User
from . import services as user_services

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        user_services.create_or_update_user_profile(instance)
