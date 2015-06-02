# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import home.models
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20150527_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(label='Von (Tage)', help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.NumberBlock(label='Bis (Tage)', help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', wagtail.wagtailcore.blocks.RichTextBlock()), ('game_results', wagtail.wagtailcore.blocks.StructBlock(())), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person-image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person-role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person-name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person-line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person-line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(label='Von (Tage)', help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.NumberBlock(label='Bis (Tage)', help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', wagtail.wagtailcore.blocks.RichTextBlock()), ('game_results', wagtail.wagtailcore.blocks.StructBlock(())), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person-image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person-role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person-name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person-line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person-line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='newsitempage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(label='Von (Tage)', help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.NumberBlock(label='Bis (Tage)', help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', wagtail.wagtailcore.blocks.RichTextBlock()), ('game_results', wagtail.wagtailcore.blocks.StructBlock(())), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person-image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person-role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person-name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person-line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person-line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='teamindex',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(label='Von (Tage)', help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.NumberBlock(label='Bis (Tage)', help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', wagtail.wagtailcore.blocks.RichTextBlock()), ('game_results', wagtail.wagtailcore.blocks.StructBlock(())), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person-image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person-role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person-name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person-line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person-line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='teampage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(label='Von (Tage)', help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.NumberBlock(label='Bis (Tage)', help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', wagtail.wagtailcore.blocks.RichTextBlock()), ('game_results', wagtail.wagtailcore.blocks.StructBlock(())), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person-image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person-role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person-name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person-line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person-line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), null=True, blank=True),
        ),
    ]
