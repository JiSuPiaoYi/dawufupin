# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-24 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fourinonedataform',
            name='month_date',
            field=models.CharField(blank=True, db_column='month_date', max_length=20),
        ),
        migrations.AddField(
            model_name='fourinonedataform',
            name='year_date',
            field=models.CharField(blank=True, db_column='year_date', max_length=20),
        ),
    ]