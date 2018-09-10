# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tt_user', '0002_auto_20180907_2032'),
        ('tt_goods', '0002_auto_20180907_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('oid', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('o_date', models.DateTimeField(auto_now=True)),
                ('isPay', models.BooleanField(default=False)),
                ('total', models.DecimalField(max_digits=6, decimal_places=2)),
                ('oaddress', models.CharField(max_length=150)),
                ('o_user', models.ForeignKey(to='tt_user.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Orderlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='tt_goods.GoodsInfo')),
                ('order', models.ForeignKey(to='tt_order.OrderInfo')),
            ],
        ),
    ]
