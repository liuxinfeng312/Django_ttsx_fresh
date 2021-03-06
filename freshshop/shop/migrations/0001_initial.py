# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-04-28 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='姓名')),
                ('password', models.CharField(max_length=255, verbose_name='密码')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='出生年月日')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=6, verbose_name='性别')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='电话')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='邮箱')),
            ],
            options={
                'db_table': 'f_user',
            },
        ),
    ]
