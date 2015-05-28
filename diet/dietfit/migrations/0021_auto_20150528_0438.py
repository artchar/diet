# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0020_auto_20150528_0426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='foods',
        ),
        migrations.RemoveField(
            model_name='mealplan',
            name='meals',
        ),
        migrations.AddField(
            model_name='mealplan',
            name='foods',
            field=models.ManyToManyField(to='dietfit.Food'),
        ),
        migrations.DeleteModel(
            name='Meal',
        ),
    ]
