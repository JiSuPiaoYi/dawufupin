# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-08-26 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel_view', '0007_template_policy_object'),
    ]

    operations = [
        migrations.AddField(
            model_name='excelapprove',
            name='status',
            field=models.SmallIntegerField(default=2, verbose_name='状态'),
        ),
    ]
