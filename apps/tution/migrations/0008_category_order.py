# Generated by Django 2.2.8 on 2020-02-08 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tution', '0007_auto_20200208_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
