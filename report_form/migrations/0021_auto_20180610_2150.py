# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-10 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_form', '0020_auto_20180610_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrativevillagedataform',
            name='town_tag',
            field=models.CharField(blank=True, db_column='town_tag', max_length=5),
        ),
        migrations.AlterField(
            model_name='administrativevillagedataform',
            name='village_tag',
            field=models.CharField(blank=True, db_column='village_tag', max_length=5),
        ),
    ]