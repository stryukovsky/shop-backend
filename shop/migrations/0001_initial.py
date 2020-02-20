# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-19 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.IntegerField(max_length=1000)),
            ],
        ),
    ]
