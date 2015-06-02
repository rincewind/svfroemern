# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20150527_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.DurationBlock(help_text='Wie weit in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.DurationBlock(help_text='Wie weit in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', wagtail.wagtailcore.blocks.RichTextBlock()), ('game_results', wagtail.wagtailcore.blocks.StructBlock(())), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person-image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person-role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person-name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person-line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person-line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='sidebar_inherit',
            field=models.BooleanField(help_text='Ist dieser Haken gesetzt, wird die Boxengasse der übergeordneten Seite übernommen. Das folgende Feld hat dann keine Bedeutung.', default=True, verbose_name='Boxengasse übernhemen'),
        ),
    ]
