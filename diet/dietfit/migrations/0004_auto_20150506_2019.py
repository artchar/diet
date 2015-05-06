# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import dietfit.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dietfit', '0003_auto_20150506_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(validators=[dietfit.models.validate_age], default=18),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='height_ft',
            field=models.IntegerField(validators=[dietfit.models.validate_height_ft], default=5),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='height_inch',
            field=models.IntegerField(validators=[dietfit.models.validate_height_inch], default=9),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weight',
            field=models.IntegerField(validators=[dietfit.models.validate_weight], default=150),
        ),
    ]
