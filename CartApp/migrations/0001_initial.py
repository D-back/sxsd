# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-09-17 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserApp', '0001_initial'),
        ('MarketApp', '0004_sxsdgoods'),
    ]

    operations = [
        migrations.CreateModel(
            name='SxsdCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_is_select', models.BooleanField(default=0)),
                ('c_goods_num', models.IntegerField()),
                ('c_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MarketApp.SxsdGoods')),
                ('c_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.SxsdUser')),
            ],
            options={
                'db_table': 'sxsd_cart',
            },
        ),
    ]