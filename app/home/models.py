import logging
import datetime

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

logger = logging.getLogger(__name__)


## renamed. might be needed by migrations until they get cleaned up
class PlaceHolderBlock(blocks.Block):
    class Meta:
        default = None
    def __init__(self, placeholder, **kwargs):
        self.placeholder = placeholder
        super().__init__(**kwargs)

class PlaceholderBlock(blocks.Block):
    class Meta:
        default = None

    def __init__(self, placeholder, **kwargs):
        self.placeholder = placeholder
        super().__init__(**kwargs)

    def render_form(self, value, prefix='', errors=None):
        return format_html('<h1>{placeholder}</h1>', placeholder=self.placeholder)

    def value_from_datadict(self, data, files, prefix):
        return self.placeholder

    def clean(self, value):
        return self.placeholder



class NumberBlock(blocks.FieldBlock):
    def __init__(self, required=True, help_text=None, **kwargs):
        self.field = fields.IntegerField(required=required, help_text=help_text)
        super().__init__(**kwargs)

class DurationBlock(blocks.FieldBlock):
    def __init__(self, required=True, help_text=None, **kwargs):
        self.field = fields.DurationField(required=required, help_text=help_text)
        super().__init__(**kwargs)

    def to_python(self, value):
        """
        Convert 'value' from a simple (JSON-serialisable) value to a (possibly complex) Python value to be
        used in the rest of the block API and within front-end templates . In simple cases this might be
        the value itself; alternatively, it might be a 'smart' version of the value which behaves mostly
        like the original value but provides a native HTML rendering when inserted into a template; or it
        might be something totally different (e.g. an image chooser will use the image ID as the clean
        value, and turn this back into an actual image object here).
        """
        return datetime.timedelta(seconds=float(value))

    def get_prep_value(self, value):
        """
        The reverse of to_python; convert the python value into JSON-serialisable form.
        """
        return value.total_seconds()




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


    @property
    def effective_sidebar(self):
        logger.debug('effective_siderbar: %s %s', self, repr(self.__class__))
        if self.sidebar_inherit:
            logger.debug('sidebar aquisition in %s', self)
            parent = self.get_parent().specific
            return parent.effective_sidebar

            # while parent:
            #     logger.debug('self: %s parent: %s %s', self, parent, repr(parent.__class__))
            #     sidebar_blocks = getattr(parent, 'effective_sidebar', None)
            #     logger.debug('sidebar: %s', repr(sidebar_blocks))
            #     if sidebar_blocks:
            #         return sidebar_blocks

            #     parent = parent.get_parent().specific
        logger.debug('sidebar, yeah!')
        return self.sidebar


    sidebar_inherit = models.BooleanField(default=True, null=False, verbose_name="Boxengasse übernhemen",
                                          help_text="Ist dieser Haken gesetzt, wird die Boxengasse der übergeordneten Seite übernommen. Das folgende Feld hat dann keine Bedeutung.")
    sidebar = StreamField([
            ('events', blocks.StructBlock([('past_cutoff', NumberBlock(help_text='Wieviele Tage in die Vergangenheit soll die Event-Box schauen', label='Von (Tage)')),
                                           ('future_cutoff', NumberBlock(help_text='Wieviele Tage in die Zukunft soll die Event-Box schauen', label='Bis (Tage)')),],
                                      label="Event-Box")),
            ('game_schedule', PlaceholderBlock('Nächste-Spiele-Box')),
            ('game_results', PlaceholderBlock('Spielergebnisse-Box')),
            ('contact', blocks.StructBlock([            
                ('person_image', ImageChooserBlock(label="Bild")),
                ('person_role', blocks.CharBlock(label="Rolle")),
                ('person_name', blocks.CharBlock(label="Name")),
                ('person_line1', blocks.CharBlock(label="Zeile 1")),
                ('person_line2', blocks.CharBlock(label="Zeile 2")),
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
                             help_text="Diese Zahl bestimmt, wieviele News-Einträge die News-Kiste anzeigt")

    base_page = blocks.PageChooserBlock(label="Zu welcher Seite?", help_text="Es werden nur Meldungen angezeigt, die unterhalb dieser Seite im Seitenbaum hängen.")

    class Meta:
        template = 'blocks/newsbox.html'
        icon = 'user'

class ContentPage(Page, SidebarMixin, ContentMixin):
    in_footer = models.ChoiceField(choices=[('right', 'rechts',), ('left', 'links'), ('nope', 'nicht im Footer')], default='nope',
                                   verbose_name="Im Fuß anzeigen?", help_text="Soll diese Seite im Fuß-Bereich angezeigt werden?")
    class Meta:
        verbose_name = "Einfache Seite"

    

class HomePage(Page, SidebarMixin):    
    
    main = StreamField([
        ('promo', blocks.ListBlock(blocks.StructBlock([
            ('text', blocks.TextBlock(label="Promo-Text", help_text="Dieser Text wird über dem Bild angezeigt")),
            ('image', ImageChooserBlock(label="Promo-Bild", help_text="Dieses Bild wird groß angezeigt"),),
            ('page', blocks.PageChooserBlock(label="Seite", help_text="Seite, welche promoted werden soll"),),
        ], label="Promos"))),        
        ('text', blocks.RichTextBlock()),
        ('news', NewsBoxBlock(label="News-Kiste")),
        ],blank=True)


    class Meta:
        verbose_name = "Homepage"
        #description = "Die erste Seite der Website. Davon sollte es nur eine geben!"

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

    @property
    def win(self):
        if self.is_home:
            return self.goals_home > self.goals_away
        else:
            return self.goals_home < self.goals_away

    def tied(self):
        return self.goals_home == self.goals_away
    
    class Meta:
        abstract = True

class TeamGame(Game, Orderable):
    team = ParentalKey('home.TeamPage', related_name='games', help_text="Spielplan")

    @property
    def team_home(self):
        if self.is_home:
            return self.team.title
        else:
            return self.opponent

    @property
    def team_away(self):
        if not self.is_home:
            return self.team.title
        else:
            return self.opponent




class TeamIndex(Page, SidebarMixin):
    subpage_types = ['home.TeamPage']
    pass

from django.utils.html import format_html




class PeopleBoxBlock(blocks.ListBlock):
    logger = logging.getLogger(__name__)
    def __init__(self, **kwargs):
        super().__init__(blocks.StructBlock([
            ('person_image', ImageChooserBlock()),
            ('person_role', blocks.CharBlock(max_length=255)),
            ('person_name', blocks.CharBlock(max_length=255)),
            ('person_line1', blocks.CharBlock(max_length=255)),
            ('person_line2', blocks.CharBlock(max_length=255)),
        ], ), **kwargs)

    
    class Meta:
        template = 'blocks/peoplebox.html'
        icon = 'user'

class TeamPage(Page, SidebarMixin):
    short_title = models.CharField("Kurzname", max_length=16, null=False, blank=True, help_text="Kurzname der Mannschaft z.B. 'A' bei der A-Jugend")
    #dfbnet = URLField()   
    content = StreamField([
        ('people', PeopleBoxBlock(label="Leute-Kiste")),
        ('text', blocks.RichTextBlock()),
        ('gameplan', PlaceholderBlock('Spielplan', label="Spielplan",)),
        ('news', NewsBoxBlock(label="News-Kiste")),
    ],null=True,blank=True)

class EventPage(Page, SidebarMixin, ContentMixin):
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
        
class NewsItemPage(Page, SidebarMixin, ContentMixin):
    teaser_text = models.TextField()
    image = models.ForeignKey(BetterImage, on_delete=models.SET_NULL, related_name='+', blank=True, null=True, help_text='Bild zur Neuigkeit (sieht immer besser aus, wenn eins dabei ist)')

    @property
    def effective_date(self):
        if self.go_live_at:
            return self.go_live_at
        if self.latest_revision_created_at:
            return self.latest_revision_created_at
        if self.first_published_at:
            return self.first_published_at

        return None # hmmm... what to do?

    class Meta:
        verbose_name = 'Meldung'
        ordering = '-go_live_at -latest_revision_created_at -first_published_at'.split()
    

HomePage.content_panels = [
    FieldPanel('title', classname='full title'),
    StreamFieldPanel('main'),
]

Basi .content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('content', classname="full"),
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
