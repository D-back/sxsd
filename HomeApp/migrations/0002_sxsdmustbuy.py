# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-09-11 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SxsdMustbuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=32)),
                ('trackid', models.IntegerField()),
            ],
            options={
                'db_table': 'sxsd_mustbuy',
            },
        ),
    ]