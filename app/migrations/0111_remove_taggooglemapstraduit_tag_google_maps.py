# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0110_auto_20160412_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taggooglemapstraduit',
            name='tag_google_maps',
        ),
    ]
