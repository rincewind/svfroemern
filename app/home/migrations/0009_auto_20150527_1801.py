# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20150527_1349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Homepage'},
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
