# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-06-30 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_center', '0002_userextra_department'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userextra',
            options={'verbose_name': '账号'},
        ),
    ]
