# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-03 20:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unbsolidaria', '0006_auto_20161203_1845'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dias',
            new_name='Dia',
        ),
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]
