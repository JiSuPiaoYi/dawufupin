# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-26 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_form', '0033_poorpeopledataform_poor_attribute'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='administrativevillagedataform',
            options={'verbose_name': '贫困村'},
        ),
        migrations.AlterModelOptions(
            name='helperdataform',
            options={'verbose_name': '帮扶人'},
        ),
        migrations.AlterModelOptions(
            name='policystaticform',
            options={'verbose_name': '政策'},
        ),
        migrations.AlterModelOptions(
            name='poorhousedataform',
            options={'verbose_name': '贫困户'},
        ),
        migrations.AlterModelOptions(
            name='poorpeopledataform',
            options={'verbose_name': '贫困人口'},
        ),
        migrations.AddField(
            model_name='policystaticform',
            name='department_tag',
            field=models.CharField(blank=True, db_column='department_tag', max_length=5),
        ),
        migrations.AlterField(
            model_name='helperdataform',
            name='helper_name',
            field=models.CharField(blank=True, db_column='helper_name', max_length=30, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='helperdataform',
            name='helper_post',
            field=models.CharField(blank=True, db_column='helper_post', max_length=50, verbose_name='职务'),
        ),
        migrations.AlterField(
            model_name='helperdataform',
            name='helper_sex',
            field=models.CharField(blank=True, db_column='helper_sex', max_length=10, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='helperdataform',
            name='helper_type',
            field=models.CharField(blank=True, db_column='helper_type', max_length=30, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='helperdataform',
            name='mobile_phone',
            field=models.CharField(blank=True, db_column='mobile_phone', max_length=100, verbose_name='手机'),
        ),
        migrations.AlterField(
            model_name='helperdataform',
            name='now_administrative_village',
            field=models.CharField(blank=True, db_column='now_administrative_village', max_length=50, verbose_name='行政村'),
        ),
        migrations.AlterField(
            model_name='helperdataform',
            name='now_village_identifier',
            field=models.CharField(blank=True, db_column='now_village_identifier', max_length=30, verbose_name='村编号'),
        ),
        migrations.AlterField(
            model_name='helperdataform',
            name='poor_home',
            field=models.CharField(blank=True, db_column='poor_home', max_length=20, verbose_name='户数'),
        ),
        migrations.AlterField(
            model_name='helperdataform',
            name='poor_name',
            field=models.CharField(blank=True, db_column='poor_name', max_length=30, verbose_name='户主姓名'),
        ),
        migrations.AlterField(
            model_name='helperdataform',
            name='poor_town',
            field=models.CharField(blank=True, db_column='poor_town', max_length=50, verbose_name='乡镇'),
        ),
        migrations.AlterField(
            model_name='helperdataform',
            name='unit_name',
            field=models.CharField(blank=True, db_column='unit_name', max_length=50, verbose_name='单位'),
        ),
        migrations.AlterField(
            model_name='helperdataform',
            name='year_date',
            field=models.CharField(blank=True, db_column='year_date', max_length=10, verbose_name='年度'),
        ),
    ]
