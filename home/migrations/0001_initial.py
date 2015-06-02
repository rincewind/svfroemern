# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailadmin.taggable
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import modelcluster.fields
from django.conf import settings
import wagtail.wagtailimages.models
import home.models
import taggit.managers
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailcore', '0013_update_golive_expire_help_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='BetterImage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
                ('file', models.ImageField(verbose_name='File', upload_to=wagtail.wagtailimages.models.get_upload_to, width_field='width', height_field='height')),
                ('width', models.IntegerField(editable=False)),
                ('height', models.IntegerField(editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('focal_point_x', models.PositiveIntegerField(null=True, blank=True)),
                ('focal_point_y', models.PositiveIntegerField(null=True, blank=True)),
                ('focal_point_width', models.PositiveIntegerField(null=True, blank=True)),
                ('focal_point_height', models.PositiveIntegerField(null=True, blank=True)),
                ('alt', models.CharField(verbose_name='Alternative', max_length=255, help_text='Wird als Alternative für dieses Bild benutzt, falls Bilder nicht angezeigt werden können (z.B. Screenreader). Sollte den Inhalt des Bildes kurz (1 Satz) beschreiben.', blank=True)),
                ('creator', models.CharField(verbose_name='Bildrechte', max_length=255, help_text='Angaben zu den Bildrechten bzw. zum Fotografen', blank=True)),
                ('tags', taggit.managers.TaggableManager(verbose_name='Tags', help_text=None, to='taggit.Tag', through='taggit.TaggedItem', blank=True)),
                ('uploaded_by_user', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, wagtail.wagtailadmin.taggable.TagSearchable),
        ),
        migrations.CreateModel(
            name='BetterImageRendition',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('file', models.ImageField(height_field='height', upload_to='images', width_field='width')),
                ('width', models.IntegerField(editable=False)),
                ('height', models.IntegerField(editable=False)),
                ('focal_point_key', models.CharField(editable=False, default='', max_length=255, blank=True)),
                ('filter', models.ForeignKey(related_name='+', to='wagtailimages.Filter')),
                ('image', models.ForeignKey(related_name='renditions', to='home.BetterImage')),
            ],
        ),
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, to='wagtailcore.Page', serialize=False)),
                ('sidebar_inherit', models.BooleanField(default=True, verbose_name='Boxengasse übernhemen', help_text='Ist dieser Haken gesetzt, wird die Boxengasse der übergeordneten Seite übernommen. Das folgende Feld hat dann keine Bedeutung.')),
                ('sidebar', wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.DurationBlock(help_text='Wie weit in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.DurationBlock(help_text='Wie weit in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', wagtail.wagtailcore.blocks.RichTextBlock()), ('game_results', wagtail.wagtailcore.blocks.StructBlock(())), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person-image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person-role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person-name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person-line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person-line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), null=True, blank=True)),
                ('content', wagtail.wagtailcore.fields.RichTextField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, to='wagtailcore.Page', serialize=False)),
                ('main', wagtail.wagtailcore.fields.StreamField((('promo', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.TextBlock(help_text='Dieser Text wird über dem Bild angezeigt', label='Promo-Text')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='Dieses Bild wird groß angezeigt', label='Promo-Bild')), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(help_text='Seite, welche promoted werden soll', label='Seite'))), label='Promos'))), ('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('news', wagtail.wagtailcore.blocks.StructBlock((('news-count', home.models.NumberBlock(help_text='Diese Anzahl bestimmt, wieviele News-Einträge die News-Box anzeigt', label='Wieviele News?')),), label='News-Box'))), blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='NewsItemPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, to='wagtailcore.Page', serialize=False)),
                ('sidebar_inherit', models.BooleanField(default=True, verbose_name='Boxengasse übernhemen', help_text='Ist dieser Haken gesetzt, wird die Boxengasse der übergeordneten Seite übernommen. Das folgende Feld hat dann keine Bedeutung.')),
                ('sidebar', wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.DurationBlock(help_text='Wie weit in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.DurationBlock(help_text='Wie weit in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', wagtail.wagtailcore.blocks.RichTextBlock()), ('game_results', wagtail.wagtailcore.blocks.StructBlock(())), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person-image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person-role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person-name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person-line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person-line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), null=True, blank=True)),
                ('content', wagtail.wagtailcore.fields.RichTextField()),
                ('teaser_text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='TeamGame',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('sort_order', models.IntegerField(editable=False, null=True, blank=True)),
                ('game_nr', models.CharField(verbose_name='Spielnr.', max_length=255, blank=True)),
                ('is_home', models.BooleanField(default=True, verbose_name='Heimspiel?')),
                ('opponent', models.CharField(verbose_name='Gegner', max_length=255)),
                ('goals_home', models.IntegerField(verbose_name='Tore Heim', null=True, blank=True)),
                ('goals_away', models.IntegerField(verbose_name='Tore Gast', null=True, blank=True)),
                ('venue', models.CharField(verbose_name='Spielort', max_length=255, null=True, blank=True)),
                ('canceled', models.BooleanField(default=False, verbose_name='Abgesagt?')),
                ('schedule', models.DateTimeField(verbose_name='Termin')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeamIndex',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, to='wagtailcore.Page', serialize=False)),
                ('sidebar_inherit', models.BooleanField(default=True, verbose_name='Boxengasse übernhemen', help_text='Ist dieser Haken gesetzt, wird die Boxengasse der übergeordneten Seite übernommen. Das folgende Feld hat dann keine Bedeutung.')),
                ('sidebar', wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.DurationBlock(help_text='Wie weit in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.DurationBlock(help_text='Wie weit in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', wagtail.wagtailcore.blocks.RichTextBlock()), ('game_results', wagtail.wagtailcore.blocks.StructBlock(())), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person-image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person-role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person-name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person-line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person-line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='TeamPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, to='wagtailcore.Page', serialize=False)),
                ('sidebar_inherit', models.BooleanField(default=True, verbose_name='Boxengasse übernhemen', help_text='Ist dieser Haken gesetzt, wird die Boxengasse der übergeordneten Seite übernommen. Das folgende Feld hat dann keine Bedeutung.')),
                ('sidebar', wagtail.wagtailcore.fields.StreamField((('events', wagtail.wagtailcore.blocks.StructBlock((('past_cutoff', home.models.DurationBlock(help_text='Wie weit in die Vergangenheit soll die Event-Box schauen')), ('future_cutoff', home.models.DurationBlock(help_text='Wie weit in die Zukunft soll die Event-Box schauen'))), label='Event-Box')), ('game_schedule', wagtail.wagtailcore.blocks.RichTextBlock()), ('game_results', wagtail.wagtailcore.blocks.StructBlock(())), ('contact', wagtail.wagtailcore.blocks.StructBlock((('person-image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Bild')), ('person-role', wagtail.wagtailcore.blocks.CharBlock(label='Rolle')), ('person-name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('person-line1', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 1')), ('person-line2', wagtail.wagtailcore.blocks.CharBlock(label='Zeile 2'))), label='Kontakt-Box'))), null=True, blank=True)),
                ('short_title', models.CharField(verbose_name='Kurzname', max_length=16, help_text="Kurzname der Mannschaft z.B. 'A' bei der A-Jugend", blank=True)),
                ('content', wagtail.wagtailcore.fields.StreamField((('people', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('person-image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('person-role', wagtail.wagtailcore.blocks.CharBlock(max_length=255)), ('person-name', wagtail.wagtailcore.blocks.CharBlock(max_length=255)), ('person-line1', wagtail.wagtailcore.blocks.CharBlock(max_length=255)), ('person-line2', wagtail.wagtailcore.blocks.CharBlock(max_length=255)))), label='Leute-Kiste')), ('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('news', home.models.NumberBlock(label='News-Kiste'))), null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.AddField(
            model_name='teamgame',
            name='team',
            field=modelcluster.fields.ParentalKey(help_text='Spielplan', to='home.TeamPage', related_name='games'),
        ),
        migrations.AlterUniqueTogether(
            name='betterimagerendition',
            unique_together=set([('image', 'filter', 'focal_point_key')]),
        ),
    ]
