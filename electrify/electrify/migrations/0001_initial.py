# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-09 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AggregatedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icp_id', models.PositiveIntegerField()),
                ('matched_amount', models.DecimalField(decimal_places=4, max_digits=6)),
                ('read_date', models.DateField()),
                ('read_time', models.TimeField()),
                ('publish_datetime', models.DateTimeField()),
                ('buyer_seller', models.CharField(choices=[(b'buyer', b'Buyer'), (b'seller', b'Seller')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='RawData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_timestamp', models.DateTimeField()),
                ('interval_read', models.DecimalField(decimal_places=3, max_digits=5)),
                ('energy_flow_direction', models.IntegerField(choices=[(0, b'Consume'), (1, b'Generate')])),
                ('icp_id', models.PositiveIntegerField()),
            ],
        ),
    ]
