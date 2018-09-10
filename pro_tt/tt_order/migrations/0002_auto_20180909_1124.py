# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tt_order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderinfo',
            old_name='isPay',
            new_name='o_isPay',
        ),
        migrations.RenameField(
            model_name='orderinfo',
            old_name='total',
            new_name='o_total',
        ),
    ]
