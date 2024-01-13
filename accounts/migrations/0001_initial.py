# Generated by Django 3.2.14 on 2024-01-13 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refresh_token', models.CharField(blank=True, max_length=255, null=True)),
                ('login', models.DateTimeField(auto_now_add=True)),
                ('logout', models.DateTimeField(blank=True, null=True)),
                ('remember_me', models.BooleanField(blank=True, null=True)),
                ('count', models.CharField(blank=True, max_length=255, null=True)),
                ('user_details', models.JSONField(blank=True, null=True)),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('secret_key', models.CharField(blank=True, max_length=255, null=True)),
                ('locked', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.BooleanField(blank=True, null=True)),
                ('tfa', models.BooleanField(blank=True, null=True)),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
