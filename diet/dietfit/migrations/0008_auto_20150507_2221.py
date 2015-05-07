# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dietfit', '0007_userprofile_calories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='calories',
            new_name='calorie_goal',
        ),
    ]
