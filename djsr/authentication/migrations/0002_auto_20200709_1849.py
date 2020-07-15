# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-09 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='fav_color',
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('CL', 'CLIENT'), ('EX', 'EXPERT')], default='CL', max_length=10),
        ),
    ]
