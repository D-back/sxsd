# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-09-16 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SxsdUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=128)),
                ('head', models.ImageField(upload_to='head')),
                ('active', models.BooleanField(default=False)),
                ('token', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'sxsd_user',
            },
        ),
    ]
