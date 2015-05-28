# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dietfit.models


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0017_userprofile_loss_goal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('calories_burned', models.FloatField(validators=[dietfit.models.validate_positive])),
            ],
        ),
        migrations.CreateModel(
            name='ExercisePlan',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('owner', models.CharField(max_length=14, default='')),
                ('exercises', models.ManyToManyField(to='dietfit.Exercise')),
            ],
        ),
    ]
