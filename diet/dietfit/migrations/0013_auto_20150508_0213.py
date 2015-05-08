# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0012_mealplan_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealplan',
            name='foods',
            field=models.ManyToManyField(to='dietfit.Food'),
        ),
    ]
