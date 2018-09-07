# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('g_title', models.CharField(max_length=20)),
                ('g_pic', models.ImageField(upload_to=b'tt_goods')),
                ('g_price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('g_unit', models.CharField(default=b'500g', max_length=10)),
                ('g_intro', models.CharField(max_length=100)),
                ('g_content', tinymce.models.HTMLField()),
                ('g_click', models.IntegerField()),
                ('g_stock', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('t_title', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='g_type',
            field=models.ForeignKey(to='tt_goods.TypeInfo'),
        ),
    ]
