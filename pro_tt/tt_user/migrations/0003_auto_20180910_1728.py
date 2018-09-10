# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tt_user', '0002_auto_20180907_2032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='ureceive',
            new_name='ureceiver',
        ),
    ]
