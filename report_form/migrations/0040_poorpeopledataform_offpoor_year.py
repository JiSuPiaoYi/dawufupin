# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-09-24 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_form', '0039_auto_20180924_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='poorpeopledataform',
            name='offpoor_year',
            field=models.CharField(blank=True, db_column='offpoor_year', max_length=20),
        ),
    ]
