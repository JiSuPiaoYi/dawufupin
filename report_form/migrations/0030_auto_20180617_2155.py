# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-17 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_form', '0029_auto_20180617_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='poorpeopleadditionalform',
            name='card_id',
            field=models.CharField(blank=True, db_column='card_id', max_length=20),
        ),
        migrations.AddField(
            model_name='poorpeopleadditionalform',
            name='card_people',
            field=models.CharField(blank=True, db_column='card_people', max_length=30),
        ),
    ]