# Generated by Django 2.2.8 on 2020-02-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tution', '0012_tution'),
    ]

    operations = [
        migrations.AddField(
            model_name='tution',
            name='batch_size',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
