# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dietfit.models


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0023_auto_20150528_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExercise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('duration', models.IntegerField(validators=[dietfit.models.validate_positive], max_length=3)),
            ],
        ),
        migrations.RenameModel(
            old_name='Exercise',
            new_name='ExerciseBase',
        ),
        migrations.AlterField(
            model_name='exerciseplan',
            name='exercises',
            field=models.ManyToManyField(to='dietfit.UserExercise'),
        ),
        migrations.AddField(
            model_name='userexercise',
            name='exercisebase',
            field=models.ForeignKey(to='dietfit.ExerciseBase'),
        ),
    ]
