import logging
import datetime

from django import template
from django.utils import timezone
from home.models import NewsItemPage, EventPage, TeamPage, Game, TeamGame, ContentPage, HomePage

register = template.Library()

logger = logging.getLogger(__name__)

@register.assignment_tag
def news_items(strhowmany, page=None):

    howmany = int(strhowmany)
    items = NewsItemPage.objects.live()

    if page:
        items = items.descendant_of(page)

    for item in items:
        yield dict(link=item.url if item.content else None, 
                   text=item.teaser_text, 
                   title=item.title, 
                   obj=item, 
                   date=item.effective_date,
                   image=item.image)


@register.assignment_tag
def events(strdaysback, strdaysfuture):

    daysback = int(strdaysback)
    daysfuture = int(strdaysfuture)
    past_cutoff = timezone.now()
    future_cutoff = past_cutoff
    past_cutoff -= datetime.timedelta(days=daysback)
    future_cutoff += datetime.timedelta(days=daysfuture)

    for item in EventPage.objects.live().filter(start__gte=past_cutoff, start__lte=future_cutoff).order_by('start'):
        logger.debug(item.__dict__)

        yield item


@register.assignment_tag
def gameplan():
    # Find the next game for every team at max. 30 days out, take the last one, 
    # go to the sunday after it (if it's not on a sunday), get all games up to that date that are unplayed.
    # I think we do that in python...

    future_cutoff = timezone.now() + datetime.timedelta(days=30)
    
    next_games = list(TeamGame.objects.filter(schedule__lte=future_cutoff, goals_home__isnull=True).order_by('schedule').all())
    teams = set(g.team.title for g in next_games if g.team.live)
    max_date = timezone.now()

    for g in next_games:
        if not teams:
            break
        teams.discard(g.team.title)
        assert max_date <= g.schedule, 'games should be ordered'
        max_date = g.schedule
        
    
    max_date += datetime.timedelta(days=7-max_date.isoweekday()) # advance to sunday

    return [g for g in next_games if g.schedule <= max_date]
    
    
@register.assignment_tag
def gameresults():
    # Find the last game for every team at max. 30 days out, take the last one, 
    # go to the sunday after it (if it's not on a sunday), get all games up to that date that are unplayed.
    # I think we do that in python...

    past_cutoff = timezone.now() - datetime.timedelta(days=30)
    min_date = timezone.now()
    next_games = list(TeamGame.objects.filter(schedule__gte=past_cutoff, schedule__lte=min_date, goals_home__isnull=False).order_by('-schedule').all())
    teams = set(g.team.title for g in next_games if g.team.live)


    for g in next_games:
        if not teams:
            break
        teams.discard(g.team.title)
        assert min_date >= g.schedule, 'games should be ordered'
        min_date = g.schedule
        
    
    min_date += datetime.timedelta(days=7-min_date.isoweekday()-7) # advance to last sunday

    return [g for g in next_games if g.schedule >= min_date]
    
    
    


@register.assignment_tag
def footer(position):
    yield from ContentPage.objects.live().filter(in_footer=position).all()


@register.assignment_tag(takes_context=True)
def menu(context, base_page=None):

    current_page = context.get('self')
    current_ancestors = current_page.get_ancestors(True) if current_page is not None else []
    logger.debug("menu for %s at %s (%s)", base_page, current_page, current_ancestors)

    if base_page is None:
        base_page = HomePage.objects.live().filter(show_in_menus=True).first()
    else:
        has_menu_descendants = base_page.get_descendants().filter(show_in_menus=True).exists()
        logger.debug('base_page descendants? %s', has_menu_descendants)
        if not has_menu_descendants:
            base_page = base_page.get_parent()
            logger.debug('new base_page: %s', base_page)
        
    if base_page is None:
        return []

    for page in base_page.get_children().live().filter(show_in_menus=True):
        logger.debug(' -> %s', page)
        if page in current_ancestors:
            yield page, True
        else:
            yield page, False
    


