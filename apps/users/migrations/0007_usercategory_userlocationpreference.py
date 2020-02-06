# Generated by Django 2.2.8 on 2020-02-05 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tution', '0005_auto_20200205_1825'),
        ('users', '0006_remove_userprofile_location_preference'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLocationPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_preference', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'At Tutor Home'), (2, 'At Student Home'), (3, 'At Insitute')], null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'location_preference')},
            },
        ),
        migrations.CreateModel(
            name='UserCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tution.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'category')},
            },
        ),
    ]