# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import home.models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20150603_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teampage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('people', home.models.PeopleBoxBlock(label='Leute-Kiste')), ('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('gameplan', home.models.PlaceholderBlock('Spielplan', label='Spielplan')), ('news', wagtail.wagtailcore.blocks.StructBlock((('news_count', home.models.NumberBlock(help_text='Diese Zahl bestimmt, wieviele News-Einträge die News-Kiste anzeigt', label='Wieviele News?')), ('base_page', wagtail.wagtailcore.blocks.PageChooserBlock(help_text='Es werden nur Meldungen angezeigt, die unterhalb dieser Seite im Seitenbaum hängen.', blank=True, label='Zu welcher Seite?'))), label='News-Kiste')), ('toc', home.models.PlaceholderBlock('Navigation', label='Navigation-Kiste'))), blank=True, null=True),
        ),
    ]
