# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-24 22:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qshock', '0003_auto_20160724_2245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caseresponse',
            old_name='occuerence_date',
            new_name='occurrence_date',
        ),
    ]
