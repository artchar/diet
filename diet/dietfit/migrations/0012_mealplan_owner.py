# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0011_userprofile_mealplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealplan',
            name='owner',
            field=models.CharField(max_length=14, default=''),
        ),
    ]
