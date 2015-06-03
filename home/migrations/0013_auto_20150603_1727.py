# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import home.models
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0015_add_more_verbose_names'),
        ('home', '0012_auto_20150528_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, auto_created=True, to='wagtailcore.Page')),
                ('sidebar_inherit', models.BooleanField(help_text='Ist dieser Haken gesetzt, wird die Boxengasse der übergeordneten Seite übernommen. Das folgende Feld hat dann keine Bedeutung.', verbose_name='Boxengasse übernhemen', default=True)),
                ('sidebar', wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.NumberBlock(label='Von (Tage)', help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.NumberBlock(label='Bis (Tage)', help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', home.models.PlaceholderBlock('Nächste-Spiele-Box')), ('game_results', home.models.PlaceholderBlock('Spielergebnisse-Box')), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person_image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person_role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person_name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person_line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person_line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), null=True, blank=True)),
                ('content', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('in_footer', models.CharField(help_text='Soll diese Seite im Fuß-Bereich angezeigt werden?', choices=[('right', 'rechts'), ('left', 'links'), ('nope', 'nicht im Footer')], max_length=20, verbose_name='Im Fuß anzeigen?', default='nope')),
            ],
            options={
                'verbose_name': 'Einfache Seite',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.AlterModelOptions(
            name='newsitempage',
            options={'ordering': ['-go_live_at', '-latest_revision_created_at', '-first_published_at'], 'verbose_name': 'Meldung'},
        ),
        migrations.AlterField(
            model_name='homepage',
            name='main',
            field=wagtail.wagtailcore.fields.StreamField((('promo', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.TextBlock(label='Promo-Text', help_text='Dieser Text wird über dem Bild angezeigt')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Promo-Bild', help_text='Dieses Bild wird groß angezeigt')), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(label='Seite', help_text='Seite, welche promoted werden soll'))), label='Promos'))), ('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('news', wagtail.wagtailcore.blocks.StructBlock((('news_count', home.models.NumberBlock(label='Wieviele News?', help_text='Diese Zahl bestimmt, wieviele News-Einträge die News-Kiste anzeigt')), ('base_page', wagtail.wagtailcore.blocks.PageChooserBlock(label='Zu welcher Seite?', help_text='Es werden nur Meldungen angezeigt, die unterhalb dieser Seite im Seitenbaum hängen.', blank=True))), label='News-Kiste'))), blank=True),
        ),
        migrations.AlterField(
            model_name='teampage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('people', home.models.PeopleBoxBlock(label='Leute-Kiste')), ('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('gameplan', home.models.PlaceholderBlock('Spielplan', label='Spielplan')), ('news', wagtail.wagtailcore.blocks.StructBlock((('news_count', home.models.NumberBlock(label='Wieviele News?', help_text='Diese Zahl bestimmt, wieviele News-Einträge die News-Kiste anzeigt')), ('base_page', wagtail.wagtailcore.blocks.PageChooserBlock(label='Zu welcher Seite?', help_text='Es werden nur Meldungen angezeigt, die unterhalb dieser Seite im Seitenbaum hängen.', blank=True))), label='News-Kiste'))), null=True, blank=True),
        ),
    ]
