# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0176_auto_20160701_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiviteNewsletter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('sent', models.DateTimeField(default=None, null=True, verbose_name='Sent', blank=True)),
                ('activite', models.ForeignKey(default=None, blank=True, to='app.Activite', null=True, verbose_name='Activity')),
                ('personne', models.ForeignKey(default=None, blank=True, to='app.Personne', null=True, verbose_name='To')),
            ],
            options={
                'ordering': ['-date_last_modif', '-date_v_debut'],
                'abstract': False,
            },
        ),
    ]
