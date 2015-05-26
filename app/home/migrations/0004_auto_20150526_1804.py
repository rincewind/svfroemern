# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20150526_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitempage',
            name='image',
            field=models.ForeignKey(null=True, blank=True, to='home.BetterImage'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='content',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='newsitempage',
            name='content',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
