# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailimages.blocks
import home.models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150523_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='main',
            field=wagtail.wagtailcore.fields.StreamField((('promo', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.TextBlock(label='Promo-Text', help_text='Dieser Text wird über dem Bild angezeigt')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Promo-Bild', help_text='Dieses Bild wird groß angezeigt')), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(label='Seite', help_text='Seite, welche promoted werden soll'))), label='Promos'))), ('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('news', wagtail.wagtailcore.blocks.StructBlock((('news_count', home.models.NumberBlock(label='Wieviele News?', help_text='Diese Anzahl bestimmt, wieviele News-Einträge die News-Box anzeigt')),), label='News-Box'))), blank=True),
        ),
    ]
