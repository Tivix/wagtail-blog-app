from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from wagtail_blog.models import BlogPost, BlogIndexPage


BlogIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('headline'),
]

BlogPost.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('author'),
    FieldPanel('date'),
    FieldPanel('date_updated'),
    FieldPanel('content', classname="full"),
    ImageChooserPanel('image'),
    FieldPanel('tags'),
]
