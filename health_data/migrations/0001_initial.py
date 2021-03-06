# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-24 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FourInOneDataForm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('people_name', models.CharField(blank=True, db_column='people_name', max_length=30)),
                ('people_id', models.CharField(blank=True, db_column='people_id', max_length=20)),
                ('people_attribute', models.CharField(blank=True, db_column='people_attribute', max_length=50)),
                ('people_address', models.CharField(blank=True, db_column='people_address', max_length=100)),
                ('people_diagnosis', models.CharField(blank=True, db_column='people_diagnosis', max_length=100)),
                ('institution_name', models.CharField(blank=True, db_column='institution_name', max_length=50)),
                ('hospitalization_number', models.CharField(blank=True, db_column='hospitalization_number', max_length=30)),
                ('in_time', models.CharField(blank=True, db_column='in_time', max_length=50)),
                ('off_time', models.CharField(blank=True, db_column='off_time', max_length=50)),
                ('medical_type', models.CharField(blank=True, db_column='medical_type', max_length=30)),
                ('medical_amount', models.CharField(blank=True, db_column='medical_amount', max_length=20)),
                ('accord_range', models.CharField(blank=True, db_column='accord_range', max_length=20)),
                ('payment_amount', models.CharField(blank=True, db_column='payment_amount', max_length=20)),
                ('medical_reimbursement', models.CharField(blank=True, db_column='medical_reimbursement', max_length=20)),
                ('insurance_indemnity', models.CharField(blank=True, db_column='insurance_indemnity', max_length=20)),
                ('civil_rescue', models.CharField(blank=True, db_column='civil_rescue', max_length=20)),
                ('supplement_indemnity', models.CharField(blank=True, db_column='supplement_indemnity', max_length=20)),
                ('hospital_undertake', models.CharField(blank=True, db_column='hospital_undertake', max_length=20)),
                ('plan_proportion', models.CharField(blank=True, db_column='plan_proportion', max_length=20)),
                ('hospital_reduction', models.CharField(blank=True, db_column='hospital_reduction', max_length=20)),
                ('people_payment', models.CharField(blank=True, db_column='people_payment', max_length=20)),
            ],
        ),
    ]
