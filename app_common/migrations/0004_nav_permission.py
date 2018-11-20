# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-05-10 20:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('app_common', '0003_nav_sort'),
    ]

    operations = [
        migrations.AddField(
            model_name='nav',
            name='permission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Permission', verbose_name='权限'),
        ),
    ]