# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dietfit.models


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0015_food_ourfood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.FloatField(validators=[dietfit.models.validate_positive]),
        ),
        migrations.AlterField(
            model_name='food',
            name='carbs',
            field=models.FloatField(validators=[dietfit.models.validate_positive]),
        ),
        migrations.AlterField(
            model_name='food',
            name='fat',
            field=models.FloatField(validators=[dietfit.models.validate_positive]),
        ),
        migrations.AlterField(
            model_name='food',
            name='protein',
            field=models.FloatField(validators=[dietfit.models.validate_positive]),
        ),
    ]
