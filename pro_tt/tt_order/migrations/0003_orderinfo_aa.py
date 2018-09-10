# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tt_order', '0002_auto_20180909_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='aa',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
