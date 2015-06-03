# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20150603_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='teampage',
            name='image',
            field=models.ForeignKey(related_name='+', null=True, to='home.BetterImage', blank=True, help_text='Mannschaftsbild', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
