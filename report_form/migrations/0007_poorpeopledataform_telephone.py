# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-05-21 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_form', '0006_auto_20180521_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='poorpeopledataform',
            name='telephone',
            field=models.CharField(blank=True, db_column='telephone', max_length=20),
        ),
    ]
