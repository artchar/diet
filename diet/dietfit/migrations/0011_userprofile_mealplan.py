# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0010_auto_20150508_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='mealplan',
            field=models.OneToOneField(default=1, to='dietfit.MealPlan'),
        ),
    ]
