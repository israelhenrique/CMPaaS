# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-27 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(max_length=254, upload_to='static/profiles'),
        ),
    ]