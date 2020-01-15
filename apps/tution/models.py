from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

class Course(models.Model):
    name = models.CharField(max_length=255)
    code = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=False)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name="user_course")

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=255)
    code = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=False)
    course = models.ManyToManyField(Course,blank=True,related_name="user_course")
    user = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name="user_subject")

    def __str__(self):
        return self.name
