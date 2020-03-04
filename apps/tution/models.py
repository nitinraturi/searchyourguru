from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from . import constants as tution_constants


class Category(models.Model):
    name = models.CharField(db_index=True, max_length=255)
    code = models.CharField(max_length=7, db_index=True, unique=True)
    tag_type = models.IntegerField(
        db_index=True, choices=tution_constants.TAG_TYPES)
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
        return self.parent.code + "-" + self.child.code


class Tution(models.Model):
    tutor = models.ForeignKey(
        get_user_model(), related_name="tution_tutor", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    price = models.FloatField()
    area = models.CharField(db_index=True, max_length=255)
    timing = models.PositiveSmallIntegerField(
        choices=tution_constants.TUTION_TIMINGS)
    location = models.PositiveSmallIntegerField(
        choices=tution_constants.LOCATION_PREFERENCE)
    batch_size = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TutionRequest(models.Model):
    tution = models.ForeignKey(Tution, on_delete=models.CASCADE)
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)
    phone = models.CharField(
        max_length=10, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['tution', 'student']

    def __str__(self):
        return str(self.id) + '-' + self.tution.tutor.email + ' - ' + self.student.email

    def tutor_email(self):
        return self.tution.tutor.email

    def student_email(self):
        return self.student.email

    def tution_title(self):
        return self.tution.title
