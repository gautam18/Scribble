# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-22 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entry', '0007_auto_20180321_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry_genre',
            name='entry',
        ),
        migrations.RemoveField(
            model_name='entry_genre',
            name='genre',
        ),
        migrations.AddField(
            model_name='entry',
            name='entry_genres',
            field=models.ManyToManyField(to='Entry.Genre'),
        ),
        migrations.DeleteModel(
            name='Entry_Genre',
        ),
    ]
