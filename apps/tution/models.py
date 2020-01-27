from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from . import constants as tution_constants

# class Course(models.Model):
#     name = models.CharField(max_length=255)
#     code = models.IntegerField(unique=True)
#     is_active = models.BooleanField(default=False)
#     user = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name="user_course")
#
#     def __str__(self):
#         return self.name
#
#
# class Subject(models.Model):
#     name = models.CharField(max_length=255)
#     code = models.IntegerField(unique=True)
#     is_active = models.BooleanField(default=False)
#     course = models.ManyToManyField(Course,blank=True,related_name="user_course")
#     user = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name="user_subject")
#
#     def __str__(self):
#         return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=7,unique=True)
    tag_type = models.IntegerField(choices=tution_constants.TAG_TYPES)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Category"

class CategoryRelation(models.Model):
    parent = models.ForeignKey(Category,related_name="tution_parent",on_delete=models.CASCADE)
    child = models.ForeignKey(Category,related_name="tution_child",on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.parent.code+"-"+self.child.code
