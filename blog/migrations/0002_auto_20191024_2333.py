# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-24 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(default='default/default.jpeg', upload_to='blog/%m-%d'),
        ),
    ]
