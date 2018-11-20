# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-05-07 21:08
from __future__ import unicode_literals

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
            name='UserExtra',
            fields=[
                ('mobile', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='联系电话')),
                ('name', models.CharField(blank=True, default='', max_length=100, verbose_name='姓名')),
                ('about', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
