# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0019_auto_20150528_0232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('foods', models.ManyToManyField(to='dietfit.Food')),
            ],
        ),
        migrations.RemoveField(
            model_name='mealplan',
            name='foods',
        ),
        migrations.AddField(
            model_name='mealplan',
            name='meals',
            field=models.ManyToManyField(to='dietfit.Meal'),
        ),
    ]
