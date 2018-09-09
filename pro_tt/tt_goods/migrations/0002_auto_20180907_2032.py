# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tt_goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodsinfo',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='typeinfo',
            options={'ordering': ['id']},
        ),
    ]
