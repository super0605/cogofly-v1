# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0081_auto_20160314_1516'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MessageThrough',
        ),
    ]
