# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dietfit.models


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0004_auto_20150506_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('calories', models.IntegerField(validators=[dietfit.models.validate_positive])),
                ('fat', models.IntegerField(validators=[dietfit.models.validate_positive])),
                ('carbs', models.IntegerField(validators=[dietfit.models.validate_positive])),
                ('protein', models.IntegerField(validators=[dietfit.models.validate_positive])),
            ],
        ),
        migrations.CreateModel(
            name='MealPlan',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('foods', models.ManyToManyField(to='dietfit.Food')),
            ],
        ),
    ]
