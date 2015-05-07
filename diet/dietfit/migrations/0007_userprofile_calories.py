# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dietfit.models


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0006_food_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='calories',
            field=models.IntegerField(default=1500, validators=[dietfit.models.validate_positive]),
        ),
    ]
