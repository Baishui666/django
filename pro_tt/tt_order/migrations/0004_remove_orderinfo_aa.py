# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tt_order', '0003_orderinfo_aa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='aa',
        ),
    ]
