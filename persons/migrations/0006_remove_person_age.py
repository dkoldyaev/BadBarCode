# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 14:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0005_auto_20170201_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='age',
        ),
    ]
