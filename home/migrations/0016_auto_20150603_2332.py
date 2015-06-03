# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_teampage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('toc', home.models.PlaceholderBlock('Navigation', label='Navigation-Kiste')), ('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(label='Von (Tage)', help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.NumberBlock(label='Bis (Tage)', help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person_image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person_role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person_name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person_line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person_line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('toc', home.models.PlaceholderBlock('Navigation', label='Navigation-Kiste')), ('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(label='Von (Tage)', help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.NumberBlock(label='Bis (Tage)', help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person_image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person_role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person_name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person_line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person_line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('toc', home.models.PlaceholderBlock('Navigation', label='Navigation-Kiste')), ('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(label='Von (Tage)', help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.NumberBlock(label='Bis (Tage)', help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person_image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person_role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person_name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person_line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person_line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsitempage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('toc', home.models.PlaceholderBlock('Navigation', label='Navigation-Kiste')), ('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(label='Von (Tage)', help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.NumberBlock(label='Bis (Tage)', help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person_image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person_role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person_name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person_line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person_line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teamindex',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('toc', home.models.PlaceholderBlock('Navigation', label='Navigation-Kiste')), ('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(label='Von (Tage)', help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.NumberBlock(label='Bis (Tage)', help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person_image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person_role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person_name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person_line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person_line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teampage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('people', home.models.PeopleBoxBlock(label='Leute-Kiste')), ('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('gameplan', home.models.PlaceholderBlock('Spielplan', label='Spielplan')), ('news', wagtail.wagtailcore.blocks.StructBlock((('news_count', home.models.NumberBlock(label='Wieviele News?', help_text='Diese Zahl bestimmt, wieviele News-Einträge die News-Kiste anzeigt')), ('base_page', wagtail.wagtailcore.blocks.PageChooserBlock(blank=True, label='Zu welcher Seite?', help_text='Es werden nur Meldungen angezeigt, die unterhalb dieser Seite im Seitenbaum hängen.'))), label='News-Kiste'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teampage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('toc', home.models.PlaceholderBlock('Navigation', label='Navigation-Kiste')), ('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(label='Von (Tage)', help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.NumberBlock(label='Bis (Tage)', help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person_image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person_role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person_name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person_line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person_line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), blank=True, null=True),
        ),
    ]
