# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-22 13:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entry', '0010_auto_20180322_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_release_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 22, 13, 2, 52, 914689), editable=False),
        ),
    ]
