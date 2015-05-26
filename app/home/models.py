import logging

from django.db import models
from django.forms import fields
from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_delete

from modelcluster.fields import ParentalKey


from wagtail.wagtailcore.models import Page, Orderable

from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.models import AbstractImage, AbstractRendition

from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel, StreamFieldPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList

from wagtail.wagtailsearch import index


class NumberBlock(blocks.FieldBlock):
    def __init__(self, required=True, help_text=None, **kwargs):
        self.field = fields.IntegerField(required=required, help_text=help_text)
        super().__init__(**kwargs)

class DurationBlock(blocks.FieldBlock):
    def __init__(self, required=True, help_text=None, **kwargs):
        self.field = fields.DurationField(required=required, help_text=help_text)
        super().__init__(**kwargs)



class BetterImage(AbstractImage):
    alt = models.CharField(verbose_name="Alternative", help_text="Wird als Alternative für dieses Bild benutzt, falls Bilder nicht angezeigt werden können (z.B. Screenreader). Sollte den Inhalt des Bildes kurz (1 Satz) beschreiben.", max_length=255, blank=True)
    creator = models.CharField(verbose_name="Bildrechte", max_length=255, blank=True, help_text="Angaben zu den Bildrechten bzw. zum Fotografen")
    
    search_fields = AbstractImage.search_fields + (
        index.SearchField('creator'),
        index.SearchField('alt'),
    )

    @property
    def default_alt_text(self):
        return self.alt

class BetterImageRendition(AbstractRendition):
    image = models.ForeignKey(BetterImage, related_name='renditions')

    class Meta:
        unique_together = (
            ('image', 'filter', 'focal_point_key'),
        )

# Receive the pre_delete sign
@receiver(pre_delete, sender=BetterImage)
def image_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.file.delete(False)

# Receive the pre_delete signal and delete the file associated with the model instance.
@receiver(pre_delete, sender=BetterImageRendition)
def rendition_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.file.delete(False)

class SidebarMixin(models.Model):
    sidebar_inherit = models.BooleanField(default=True, null=False, verbose_name="Boxengasse übernhemen",
                                          help_text="Ist dieser Haken gesetzt, wird die Boxengasse der übergeordneten Seite übernommen. Das folgende Feld hat dann keine Bedeutung.")
    sidebar = StreamField([
            ('events', blocks.StructBlock([('past_cutoff', DurationBlock(help_text='Wie weit in die Vergangenheit soll die Event-Box schauen')),
                                           ('future_cutoff', DurationBlock(help_text='Wie weit in die Zukunft soll die Event-Box schauen')),],
                                      label="Event-Box")),
            ('game_schedule', blocks.RichTextBlock()),
            ('game_results', blocks.StructBlock()),
            ('contact', blocks.StructBlock([            
                ('person-image', ImageChooserBlock(label="Bild")),
                ('person-role', blocks.CharBlock(label="Rolle")),
                ('person-name', blocks.CharBlock(label="Name")),
                ('person-line1', blocks.CharBlock(label="Zeile 1")),
                ('person-line2', blocks.CharBlock(label="Zeile 2")),
            ], label="Kontakt-Box")),
        ],null=True,blank=True)
    
    class Meta:
        abstract = True        

    sidebar_panels = [
        FieldPanel('sidebar_inherit'),
        StreamFieldPanel('sidebar'),
    ]

class ContentMixin(models.Model):
    content = RichTextField(blank=True)

    class Meta:
        abstract = True


class NewsBoxBlock(blocks.StructBlock):
    logger = logging.getLogger(__name__)
    news_count = NumberBlock(label="Wieviele News?",
                             help_text="Diese Anzahl bestimmt, wieviele News-Einträge die News-Box anzeigt")

    class Meta:
        template = 'blocks/newsbox.html'
        icon = 'user'


class HomePage(Page):    
    
    sidebar_panels = []
    main = StreamField([
        ('promo', blocks.ListBlock(blocks.StructBlock([
            ('text', blocks.TextBlock(label="Promo-Text", help_text="Dieser Text wird über dem Bild angezeigt")),
            ('image', ImageChooserBlock(label="Promo-Bild", help_text="Dieses Bild wird groß angezeigt"),),
            ('page', blocks.PageChooserBlock(label="Seite", help_text="Seite, welche promoted werden soll"),),
        ], label="Promos"))),        
        ('text', blocks.RichTextBlock()),
        ('news', NewsBoxBlock(label="News-Box")),
        ],blank=True)

class Game(models.Model):
    game_nr = models.CharField('Spielnr.', max_length=255, blank=True, null=False)
    is_home = models.BooleanField('Heimspiel?', default=True, null=False)
    opponent = models.CharField('Gegner', max_length=255, blank=False, null=False)
    goals_home = models.IntegerField('Tore Heim', blank=True, null=True)
    goals_away = models.IntegerField('Tore Gast', blank=True, null=True)
    venue = models.CharField('Spielort', max_length=255, blank=True, null=True)
    canceled = models.BooleanField('Abgesagt?', default=False)
    schedule = models.DateTimeField('Termin')

    panels = [
        FieldPanel('game_nr'),
        FieldPanel('is_home'),
        FieldPanel('opponent'),
        FieldPanel('goals_home'),
        FieldPanel('goals_away'),
        FieldPanel('venue'),
        FieldPanel('canceled'),
        FieldPanel('schedule'),
    ]
    
    class Meta:
        abstract = True

class TeamGame(Game, Orderable):
    team = ParentalKey('home.TeamPage', related_name='games', help_text="Spielplan")


class TeamIndex(Page, SidebarMixin):
    pass

class TeamPage(Page, SidebarMixin):
    short_title = models.CharField("Kurzname", max_length=16, null=False, blank=True, help_text="Kurzname der Mannschaft z.B. 'A' bei der A-Jugend")
    #dfbnet = URLField()   
    content = StreamField([
        ('people', blocks.ListBlock(blocks.StructBlock([
            ('person-image', ImageChooserBlock()),
            ('person-role', blocks.CharBlock(max_length=255)),
            ('person-name', blocks.CharBlock(max_length=255)),
            ('person-line1', blocks.CharBlock(max_length=255)),
            ('person-line2', blocks.CharBlock(max_length=255)),
        ], ), label="Leute-Kiste")),                            
        ('text', blocks.RichTextBlock()),
        ('news', NumberBlock(label="News-Kiste")),
    ],null=True,blank=True)

class EventPage(Page, SidebarMixin, ContentMixin):
    start = models.DateTimeField()
    end = models.DateTimeField()
        
class NewsItemPage(Page, SidebarMixin, ContentMixin):
    teaser_text = models.TextField()
    image = models.ForeignKey(BetterImage, on_delete=models.SET_NULL, related_name='+', blank=True, null=True, help_text='Bild zur Neuigkeit (sieht immer besser aus, wenn eins dabei ist)')
    

HomePage.content_panels = [
    FieldPanel('title', classname='full title'),
    StreamFieldPanel('main'),
]

NewsItemPage.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('teaser_text', classname='full'),
    ImageChooserPanel('image',),
    FieldPanel('content', classname="full"),
]

EventPage.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('start', classname='full'  ),
    FieldPanel('end', classname='full'),
    FieldPanel('content', classname="full"),
]

TeamPage.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('short_title', classname='full'),
    StreamFieldPanel('content'),
    InlinePanel('games', panels=TeamGame.panels, label="Spiele"),
]

for page in HomePage, TeamPage, EventPage, NewsItemPage:
    page.edit_handler = TabbedInterface([
        ObjectList(page.content_panels, heading='Inhalt'),    
        ObjectList(page.sidebar_panels, heading='Boxengasse'),
        ObjectList(page.promote_panels, heading='Promo'),
        ObjectList(page.settings_panels, heading='Einstellungen'),])
