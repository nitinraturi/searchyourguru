# Generated by Django 2.2.8 on 2020-02-05 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tution', '0004_usercategory_userlocationpreference'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userlocationpreference',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='userlocationpreference',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserCategory',
        ),
        migrations.DeleteModel(
            name='UserLocationPreference',
        ),
    ]
