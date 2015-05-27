# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dietfit.models


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0016_auto_20150508_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='loss_goal',
            field=models.IntegerField(default=0, validators=[dietfit.models.validate_positive]),
        ),
    ]
