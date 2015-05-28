# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dietfit.models


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0021_auto_20150528_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.DecimalField(validators=[dietfit.models.validate_positive], decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='food',
            name='carbs',
            field=models.DecimalField(validators=[dietfit.models.validate_positive], decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='food',
            name='fat',
            field=models.DecimalField(validators=[dietfit.models.validate_positive], decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='food',
            name='protein',
            field=models.DecimalField(validators=[dietfit.models.validate_positive], decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='food',
            name='servingsize',
            field=models.CharField(max_length=15, default='1 serving'),
        ),
    ]
