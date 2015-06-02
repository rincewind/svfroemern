# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import home.models
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20150528_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='main',
            field=wagtail.wagtailcore.fields.StreamField((('promo', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.TextBlock(label='Promo-Text', help_text='Dieser Text wird über dem Bild angezeigt')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Promo-Bild', help_text='Dieses Bild wird groß angezeigt')), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(label='Seite', help_text='Seite, welche promoted werden soll'))), label='Promos'))), ('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('news', wagtail.wagtailcore.blocks.StructBlock((('news_count', home.models.NumberBlock(label='Wieviele News?', help_text='Diese Zahl bestimmt, wieviele News-Einträge die News-Kiste anzeigt')), ('base_page', wagtail.wagtailcore.blocks.PageChooserBlock(label='Zu welcher Seite?', help_text='Es werden nur Meldungen angezeigt, die unterhalb dieser Seite im Seitenbaum hängen.'))), label='News-Kiste'))), blank=True),
        ),
        migrations.AlterField(
            model_name='teampage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('people', home.models.PeopleBoxBlock(label='Leute-Kiste')), ('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('gameplan', home.models.PlaceholderBlock('Spielplan', label='Spielplan')), ('news', wagtail.wagtailcore.blocks.StructBlock((('news_count', home.models.NumberBlock(label='Wieviele News?', help_text='Diese Zahl bestimmt, wieviele News-Einträge die News-Kiste anzeigt')), ('base_page', wagtail.wagtailcore.blocks.PageChooserBlock(label='Zu welcher Seite?', help_text='Es werden nur Meldungen angezeigt, die unterhalb dieser Seite im Seitenbaum hängen.'))), label='News-Kiste'))), null=True, blank=True),
        ),
    ]
