# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-01 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_form', '0015_auto_20180531_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='helperdataform',
            name='year_date',
            field=models.CharField(blank=True, db_column='year_date', max_length=10),
        ),
    ]
