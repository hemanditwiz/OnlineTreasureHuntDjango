# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-08 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunt', '0003_remove_usermodel_reg_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='super_user',
            field=models.BooleanField(default=False),
        ),
    ]