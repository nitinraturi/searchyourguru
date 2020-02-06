from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from . import constants as tution_constants


class Category(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=7, db_index=True, unique=True)
    tag_type = models.IntegerField(choices=tution_constants.TAG_TYPES)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Category"


class CategoryRelation(models.Model):
    parent = models.ForeignKey(
        Category, related_name="tution_parent", on_delete=models.CASCADE)
    child = models.ForeignKey(
        Category, related_name="tution_child", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.parent.code+"-"+self.child.code
