# Generated by Django 2.2.8 on 2020-02-16 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20200214_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='price_per_hour',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='qualification',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='timing',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='zipcode',
        ),
    ]