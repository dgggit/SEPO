# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-21 13:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0005_auto_20180521_2209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mymodel',
            name='author',
        ),
    ]
