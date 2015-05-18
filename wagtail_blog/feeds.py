import re

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed

from models import BlogPage


class BlogPostRSSFeed(Feed):
    title = 'RSS Feed'
    description = ''

    def items(self):
        return BlogPage.objects.live().order_by('-date')[:50]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        desc = re.compile(r'<.*?>').sub('', item.content)
        if len(desc) > 250:
            desc = desc[250] + '...'

        return desc


class BlogPostAtomFeed(BlogPostRSSFeed):
    title = 'Atom Feed'
    feed_type = Atom1Feed
    subtitle = BlogPostRSSFeed.description
