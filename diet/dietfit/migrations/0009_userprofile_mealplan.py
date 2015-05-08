# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0008_auto_20150507_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='mealplan',
            field=models.OneToOneField(to='dietfit.MealPlan', default=1),
        ),
    ]
