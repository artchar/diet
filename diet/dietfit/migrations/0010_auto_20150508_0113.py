# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0009_userprofile_mealplan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='mealplan',
        ),
        migrations.AlterField(
            model_name='mealplan',
            name='foods',
            field=models.ManyToManyField(to='dietfit.Food', default=1),
        ),
    ]
