# Generated by Django 2.2.8 on 2020-02-04 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tution', '0002_auto_20200204_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.CharField(db_index=True, max_length=7, unique=True),
        ),
    ]