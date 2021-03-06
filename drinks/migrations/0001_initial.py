# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 20:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0003_auto_20170125_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Person')),
            ],
            options={
                'verbose_name': 'Дринк',
                'verbose_name_plural': 'Дринки',
            },
        ),
    ]
