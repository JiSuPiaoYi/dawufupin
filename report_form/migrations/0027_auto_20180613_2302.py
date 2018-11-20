# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-13 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_form', '0026_policystaticform_implement_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrativevillageadditionalform',
            name='date',
        ),
        migrations.RemoveField(
            model_name='poorhouseadditionalform',
            name='date',
        ),
        migrations.RemoveField(
            model_name='poorpeopleadditionalform',
            name='date',
        ),
        migrations.AddField(
            model_name='administrativevillageadditionalform',
            name='date_month',
            field=models.CharField(blank=True, db_column='date_month', max_length=20),
        ),
        migrations.AddField(
            model_name='administrativevillageadditionalform',
            name='date_year',
            field=models.CharField(blank=True, db_column='date_year', max_length=20),
        ),
        migrations.AddField(
            model_name='poorhouseadditionalform',
            name='date_month',
            field=models.CharField(blank=True, db_column='date_month', max_length=20),
        ),
        migrations.AddField(
            model_name='poorhouseadditionalform',
            name='date_year',
            field=models.CharField(blank=True, db_column='date_year', max_length=20),
        ),
        migrations.AddField(
            model_name='poorpeopleadditionalform',
            name='date_month',
            field=models.CharField(blank=True, db_column='date_month', max_length=20),
        ),
        migrations.AddField(
            model_name='poorpeopleadditionalform',
            name='date_year',
            field=models.CharField(blank=True, db_column='date_year', max_length=20),
        ),
    ]