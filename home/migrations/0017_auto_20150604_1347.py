# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.blocks
import home.models
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20150603_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('toc', home.models.PlaceholderBlock('Navigation', label='Navigation-Kiste')), ('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(label='Von (Tage)', default=5, help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.NumberBlock(label='Bis (Tage)', default=60, help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person_image', wagtail.wagtailimages.blocks.ImageChooserBlock(blank=True, null=True, label='Bild')), ('person_role', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Rolle')), ('person_name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person_line1', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Zeile 1')), ('person_line2', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Zeile 2'))), label='Kontakt-Box'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('toc', home.models.PlaceholderBlock('Navigation', label='Navigation-Kiste')), ('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(label='Von (Tage)', default=5, help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.NumberBlock(label='Bis (Tage)', default=60, help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person_image', wagtail.wagtailimages.blocks.ImageChooserBlock(blank=True, null=True, label='Bild')), ('person_role', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Rolle')), ('person_name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person_line1', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Zeile 1')), ('person_line2', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Zeile 2'))), label='Kontakt-Box'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='main',
            field=wagtail.wagtailcore.fields.StreamField((('promo', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.TextBlock(blank=True, help_text='Dieser Text wird über dem Bild angezeigt', label='Promo-Text')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='Dieses Bild wird groß angezeigt', label='Promo-Bild')), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(help_text='Seite, welche promoted werden soll', label='Seite'))), label='Promos'), template='blocks/promobox.html')), ('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('news', wagtail.wagtailcore.blocks.StructBlock((('news_count', home.models.NumberBlock(help_text='Diese Zahl bestimmt, wieviele News-Einträge die News-Kiste anzeigt', default=12, label='Wieviele News?')), ('base_page', wagtail.wagtailcore.blocks.PageChooserBlock(blank=True, null=True, help_text='Es werden nur Meldungen angezeigt, die unterhalb dieser Seite im Seitenbaum hängen.', label='Zu welcher Seite?'))), label='News-Kiste'))), blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('toc', home.models.PlaceholderBlock('Navigation', label='Navigation-Kiste')), ('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(label='Von (Tage)', default=5, help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.NumberBlock(label='Bis (Tage)', default=60, help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person_image', wagtail.wagtailimages.blocks.ImageChooserBlock(blank=True, null=True, label='Bild')), ('person_role', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Rolle')), ('person_name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person_line1', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Zeile 1')), ('person_line2', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Zeile 2'))), label='Kontakt-Box'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsitempage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('toc', home.models.PlaceholderBlock('Navigation', label='Navigation-Kiste')), ('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(label='Von (Tage)', default=5, help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.NumberBlock(label='Bis (Tage)', default=60, help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person_image', wagtail.wagtailimages.blocks.ImageChooserBlock(blank=True, null=True, label='Bild')), ('person_role', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Rolle')), ('person_name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person_line1', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Zeile 1')), ('person_line2', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Zeile 2'))), label='Kontakt-Box'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teamindex',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('toc', home.models.PlaceholderBlock('Navigation', label='Navigation-Kiste')), ('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(label='Von (Tage)', default=5, help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.NumberBlock(label='Bis (Tage)', default=60, help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person_image', wagtail.wagtailimages.blocks.ImageChooserBlock(blank=True, null=True, label='Bild')), ('person_role', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Rolle')), ('person_name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person_line1', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Zeile 1')), ('person_line2', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Zeile 2'))), label='Kontakt-Box'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teampage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('people', home.models.PeopleBoxBlock(label='Leute-Kiste')), ('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('gameplan', home.models.PlaceholderBlock('Spielplan', label='Spielplan')), ('news', wagtail.wagtailcore.blocks.StructBlock((('news_count', home.models.NumberBlock(help_text='Diese Zahl bestimmt, wieviele News-Einträge die News-Kiste anzeigt', default=12, label='Wieviele News?')), ('base_page', wagtail.wagtailcore.blocks.PageChooserBlock(blank=True, null=True, help_text='Es werden nur Meldungen angezeigt, die unterhalb dieser Seite im Seitenbaum hängen.', label='Zu welcher Seite?'))), label='News-Kiste'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teampage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField((('toc', home.models.PlaceholderBlock('Navigation', label='Navigation-Kiste')), ('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(label='Von (Tage)', default=5, help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.NumberBlock(label='Bis (Tage)', default=60, help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person_image', wagtail.wagtailimages.blocks.ImageChooserBlock(blank=True, null=True, label='Bild')), ('person_role', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Rolle')), ('person_name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person_line1', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Zeile 1')), ('person_line2', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Zeile 2'))), label='Kontakt-Box'))), blank=True, null=True),
        ),
    ]
