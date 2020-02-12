from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from . import constants as tution_constants


class Category(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=7, db_index=True, unique=True)
    tag_type = models.IntegerField(choices=tution_constants.TAG_TYPES)
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Category"


class CategoryRelation(models.Model):
    parent = models.ForeignKey(
        Category, related_name="tution_parent", on_delete=models.CASCADE)
    child = models.ForeignKey(
        Category, related_name="tution_child", on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.parent.code+"-"+self.child.code


class TutionRequest(models.Model):
    tutor = models.ForeignKey(get_user_model(
    ), related_name="tution_request_user1", on_delete=models.CASCADE)
    student = models.ForeignKey(get_user_model(
    ), related_name="tution_request_user2", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_accepted = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.tutor.email)+str(self.student.email)
