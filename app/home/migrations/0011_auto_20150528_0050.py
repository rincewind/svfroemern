# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import home.models
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20150527_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen', label='Von (Tage)')), ('future_cutoff', home.models.NumberBlock(help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen', label='Bis (Tage)'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person_image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person_role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person_name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person_line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person_line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen', label='Von (Tage)')), ('future_cutoff', home.models.NumberBlock(help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen', label='Bis (Tage)'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person_image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person_role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person_name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person_line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person_line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='newsitempage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen', label='Von (Tage)')), ('future_cutoff', home.models.NumberBlock(help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen', label='Bis (Tage)'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person_image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person_role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person_name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person_line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person_line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='teamindex',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen', label='Von (Tage)')), ('future_cutoff', home.models.NumberBlock(help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen', label='Bis (Tage)'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person_image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person_role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person_name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person_line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person_line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='teampage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen', label='Von (Tage)')), ('future_cutoff', home.models.NumberBlock(help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen', label='Bis (Tage)'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person_image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person_role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person_name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person_line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person_line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), null=True, blank=True),
        ),
    ]
