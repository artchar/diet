# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dietfit.models


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0018_exercise_exerciseplan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exerciseplan',
            name='exercises',
        ),
        migrations.AddField(
            model_name='food',
            name='servingsize',
            field=models.IntegerField(default=1, validators=[dietfit.models.validate_positive]),
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
        migrations.DeleteModel(
            name='ExercisePlan',
        ),
    ]
