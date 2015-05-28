# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dietfit.models


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0022_auto_20150528_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('met', models.DecimalField(max_digits=5, validators=[dietfit.models.validate_positive], decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='ExercisePlan',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('owner', models.CharField(default='', max_length=14)),
                ('exercises', models.ManyToManyField(to='dietfit.Exercise')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='exerciseplan',
            field=models.OneToOneField(to='dietfit.ExercisePlan', null=True),
        ),
    ]
