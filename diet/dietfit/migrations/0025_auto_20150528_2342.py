# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dietfit.models


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0024_auto_20150528_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeightExercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='weight exercise', max_length=14)),
                ('weight', models.IntegerField(default=0, validators=[dietfit.models.validate_positive])),
                ('reps', models.IntegerField(default=0, validators=[dietfit.models.validate_positive])),
                ('sets', models.IntegerField(default=0, validators=[dietfit.models.validate_positive])),
            ],
        ),
        migrations.CreateModel(
            name='WeightPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.CharField(default='', max_length=14)),
                ('workout_time', models.IntegerField(default=0, validators=[dietfit.models.validate_positive])),
                ('high_intensity', models.BooleanField(default=False)),
                ('weightExercises', models.ManyToManyField(to='dietfit.WeightExercise', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='weightplan',
            field=models.OneToOneField(to='dietfit.WeightPlan', null=True),
        ),
    ]
