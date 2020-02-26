# Generated by Django 2.2.8 on 2020-02-25 06:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tution', '0015_auto_20200223_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutionRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tution.Tution')),
            ],
            options={
                'unique_together': {('tution', 'student')},
            },
        ),
    ]