# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0185_auto_20160713_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagtraduit',
            name='poids',
            field=models.IntegerField(default=None, help_text='Used for ordering', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personne',
            name='langue',
            field=models.IntegerField(default=None, null=True, blank=True, choices=[(0, 'Albanian'), (1, 'German'), (2, 'English'), (3, 'Arabic'), (4, 'Armenian'), (5, 'Bengali'), (6, 'Catalan'), (7, 'Chinese'), (8, 'Korean'), (9, 'Croatian'), (10, 'Danish'), (11, 'Spanish'), (12, 'Finnish'), (13, 'French'), (14, 'Greek'), (15, 'Hungarian'), (16, 'Italian'), (17, 'Malaysian'), (18, 'Mongolian'), (19, 'Dutch'), (20, 'Occitan'), (21, 'Persian'), (22, 'Portuguese'), (23, 'Romanian'), (24, 'Russian'), (25, 'Serbian'), (26, 'Slovakian'), (27, 'Slovenian'), (28, 'Swedish'), (29, 'Turkish'), (30, 'Other')]),
        ),
        migrations.AlterField(
            model_name='tagtraduit',
            name='tag',
            field=models.ForeignKey(related_name='tag', default=None, blank=True, to='app.TagBase', help_text="It's the master tag", null=True),
        ),
    ]
