# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-09-28 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_common', '0014_feedbacks_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbacks',
            name='about_object_type',
            field=models.SmallIntegerField(default=0, verbose_name='涉及对象类型'),
        ),
    ]
