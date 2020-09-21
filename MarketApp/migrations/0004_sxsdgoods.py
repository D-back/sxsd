# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-09-11 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarketApp', '0003_auto_20200911_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='SxsdGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField()),
                ('productimg', models.CharField(max_length=64)),
                ('productname', models.CharField(max_length=128)),
                ('productlongname', models.CharField(max_length=128)),
                ('isxf', models.IntegerField()),
                ('pmdesc', models.IntegerField()),
                ('specifics', models.CharField(max_length=32)),
                ('price', models.FloatField()),
                ('marketprice', models.FloatField()),
                ('categoryid', models.IntegerField()),
                ('childcid', models.IntegerField()),
                ('childcidname', models.CharField(max_length=32)),
                ('dealerid', models.IntegerField()),
                ('storenums', models.IntegerField()),
                ('productnum', models.IntegerField()),
            ],
            options={
                'db_table': 'sxsd_goods',
            },
        ),
    ]