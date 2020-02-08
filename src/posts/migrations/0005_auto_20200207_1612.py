# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-02-07 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200207_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='height_field',
            field=models.PositiveIntegerField(blank=True, default='200', editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=posts.models.upload_location, width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='post',
            name='width_field',
            field=models.PositiveIntegerField(blank=True, default='200', editable=False, null=True),
        ),
    ]