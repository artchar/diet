# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0005_food_mealplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='name',
            field=models.CharField(default='food', max_length=30),
        ),
    ]
