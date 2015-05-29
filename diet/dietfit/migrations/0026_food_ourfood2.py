# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0025_auto_20150528_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='ourfood2',
            field=models.BooleanField(default=False),
        ),
    ]
