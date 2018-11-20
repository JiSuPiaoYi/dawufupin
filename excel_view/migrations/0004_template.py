# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-07-29 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel_view', '0003_auto_20180729_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='上传时间')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('row', models.TextField(blank=True, null=True, verbose_name='列字段')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '模板管理',
            },
        ),
    ]
