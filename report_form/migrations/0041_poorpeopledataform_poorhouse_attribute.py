# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-09-24 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_form', '0040_poorpeopledataform_offpoor_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='poorpeopledataform',
            name='poorhouse_attribute',
            field=models.CharField(blank=True, db_column='poorhouse_attribute', max_length=30),
        ),
    ]