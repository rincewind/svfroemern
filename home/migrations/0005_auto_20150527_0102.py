# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import django.db.models.deletion
import home.models
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20150526_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='main',
            field=wagtail.wagtailcore.fields.StreamField((('promo', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.TextBlock(help_text='Dieser Text wird über dem Bild angezeigt', label='Promo-Text')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='Dieses Bild wird groß angezeigt', label='Promo-Bild')), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(help_text='Seite, welche promoted werden soll', label='Seite'))), label='Promos'))), ('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('news', wagtail.wagtailcore.blocks.StructBlock((('news_count', home.models.NumberBlock(help_text='Diese Zahl bestimmt, wieviele News-Einträge die News-Kiste anzeigt', label='Wieviele News?')),), label='News-Kiste'))), blank=True),
        ),
        migrations.AlterField(
            model_name='newsitempage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, to='home.BetterImage', related_name='+', help_text='Bild zur Neuigkeit (sieht immer besser aus, wenn eins dabei ist)', on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AlterField(
            model_name='teampage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('people', home.models.PeopleBoxBlock(label='Leute-Kiste')), ('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('news', wagtail.wagtailcore.blocks.StructBlock((('news_count', home.models.NumberBlock(help_text='Diese Zahl bestimmt, wieviele News-Einträge die News-Kiste anzeigt', label='Wieviele News?')),), label='News-Kiste'))), blank=True, null=True),
        ),
    ]
