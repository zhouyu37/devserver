# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-01-02 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disk',
            name='model',
            field=models.CharField(max_length=128, verbose_name='\u78c1\u76d8\u578b\u53f7'),
        ),
    ]