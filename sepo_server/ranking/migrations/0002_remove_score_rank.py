# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-25 11:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='rank',
        ),
    ]