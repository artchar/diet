# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0014_auto_20150508_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='ourfood',
            field=models.BooleanField(default=False),
        ),
    ]
