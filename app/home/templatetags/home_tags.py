import logging

from django import template
from home.models import NewsItemPage

register = template.Library()

logger = logging.getLogger(__name__)

@register.assignment_tag
def news_items(strhowmany):
    howmany = int(strhowmany)

    for item in NewsItemPage.objects.all():
        logger.debug(item.__dict__)

        yield dict(link=item.url, 
                   text=item.teaser_text, 
                   title=item.title, 
                   obj=item, 
                   date=item.latest_revision_created_at,
                   image=item.image)


