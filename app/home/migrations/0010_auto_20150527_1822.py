# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20150527_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen', label='Von (Tage)')), ('future_cutoff', home.models.NumberBlock(help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen', label='Bis (Tage)'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person-image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person-role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person-name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person-line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person-line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen', label='Von (Tage)')), ('future_cutoff', home.models.NumberBlock(help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen', label='Bis (Tage)'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person-image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person-role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person-name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person-line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person-line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='newsitempage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen', label='Von (Tage)')), ('future_cutoff', home.models.NumberBlock(help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen', label='Bis (Tage)'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person-image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person-role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person-name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person-line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person-line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='teamindex',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen', label='Von (Tage)')), ('future_cutoff', home.models.NumberBlock(help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen', label='Bis (Tage)'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person-image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person-role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person-name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person-line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person-line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='teampage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('people', home.models.PeopleBoxBlock(label='Leute-Kiste')), ('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('gameplan', home.models.PlaceholderBlock('Spielplan', label='Spielplan')), ('news', wagtail.wagtailcore.blocks.StructBlock((('news_count', home.models.NumberBlock(help_text='Diese Zahl bestimmt, wieviele News-Einträge die News-Kiste anzeigt', label='Wieviele News?')),), label='News-Kiste'))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='teampage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen', label='Von (Tage)')), ('future_cutoff', home.models.NumberBlock(help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen', label='Bis (Tage)'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person-image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person-role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person-name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person-line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person-line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), null=True, blank=True),
        ),
    ]
