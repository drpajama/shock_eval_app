# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-24 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qshock', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caseresponse',
            old_name='answer_responder1',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='caseresponse',
            old_name='note_responder1',
            new_name='note',
        ),
        migrations.RenameField(
            model_name='caseresponse',
            old_name='marking1',
            new_name='tag1',
        ),
        migrations.RenameField(
            model_name='caseresponse',
            old_name='marking2',
            new_name='tag2',
        ),
        migrations.RemoveField(
            model_name='caseresponse',
            name='answer_responder2',
        ),
        migrations.RemoveField(
            model_name='caseresponse',
            name='answer_responder3',
        ),
        migrations.RemoveField(
            model_name='caseresponse',
            name='answer_responder4',
        ),
        migrations.RemoveField(
            model_name='caseresponse',
            name='note_responder2',
        ),
        migrations.RemoveField(
            model_name='caseresponse',
            name='note_responder3',
        ),
        migrations.RemoveField(
            model_name='caseresponse',
            name='note_responder4',
        ),
        migrations.AddField(
            model_name='caseresponse',
            name='responder_id',
            field=models.IntegerField(default=0),
        ),
    ]
