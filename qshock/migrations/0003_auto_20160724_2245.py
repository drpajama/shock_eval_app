# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-24 22:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qshock', '0002_auto_20160724_2225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caseresponse',
            old_name='occurence_date',
            new_name='occuerence_date',
        ),
    ]
