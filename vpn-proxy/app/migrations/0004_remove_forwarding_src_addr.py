# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 08:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160713_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forwarding',
            name='src_addr',
        ),
    ]
