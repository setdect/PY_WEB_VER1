# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-08 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create Date'),
        ),
        migrations.AddField(
            model_name='post',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Modify Date'),
        ),
    ]
