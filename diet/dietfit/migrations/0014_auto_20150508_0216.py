# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0013_auto_20150508_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mealplan',
            field=models.OneToOneField(to='dietfit.MealPlan'),
        ),
    ]
