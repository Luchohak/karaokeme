# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-01 04:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songmanager',
            name='first_name',
            field=models.CharField(default=b'Jhon', max_length=30),
        ),
        migrations.AddField(
            model_name='songmanager',
            name='last_name',
            field=models.CharField(default=b'Doe', max_length=30),
        ),
        migrations.AddField(
            model_name='songmanager',
            name='password',
            field=models.CharField(default=b'password', max_length=30),
        ),
        migrations.AddField(
            model_name='songmanager',
            name='username',
            field=models.CharField(default=b'username', max_length=30),
        ),
        migrations.AlterField(
            model_name='songmanager',
            name='user',
            field=models.OneToOneField(default=b'admin', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
