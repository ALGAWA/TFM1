# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TFM1app', '0003_activbcn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activbcn',
            name='idevento',
            field=models.CharField(max_length=30),
        ),
    ]
