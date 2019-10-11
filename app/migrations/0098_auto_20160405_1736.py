# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0097_auto_20160405_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagbase',
            name='type_tag',
            field=models.IntegerField(default=None, null=True, blank=True, choices=[(1, 'Diplomas'), (2, 'Activities'), (3, 'Hobbies'), (4, 'Driving licences'), (5, 'Personality'), (6, 'Language')]),
        ),
    ]
