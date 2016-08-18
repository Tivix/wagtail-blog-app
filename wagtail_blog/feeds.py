import re

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.conf import settings

from wagtail_blog.models import BlogPost


class BlogPostRSSFeed(Feed):
    title = getattr(settings, 'WAGTAIL_BLOG_FEED_TITLE', "RSS Feed")
    link = getattr(settings, 'WAGTAIL_BLOG_FEED_LINK', "/blog/"),
    description = getattr(settings, 'WAGTAIL_BLOG_FEED_DESCRIPTION', "Blog Post Feed")

    def items(self):
        return BlogPost.objects.live().order_by('-date')[:getattr(settings, 'WAGTAIL_BLOG_FEED_LENGTH', 50)]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        desc = re.compile(r'<.*?>').sub('', item.content)
        if len(desc) > 250:
            desc = desc[:250] + '...'

        return desc

    def item_link(self, item):
        return item.url


class BlogPostAtomFeed(BlogPostRSSFeed):
    title = getattr(settings, 'WAGTAIL_BLOG_FEED_TITLE', 'Atom Feed')
    feed_type = Atom1Feed
    subtitle = BlogPostRSSFeed.description
