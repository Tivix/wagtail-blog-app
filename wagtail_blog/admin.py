from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from models import BlogPage, BlogIndexPage


# Add your Wagtail panels here.
BlogIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('headline'),
]

BlogPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('author'),
    FieldPanel('date'),
    FieldPanel('date_updated'),
    FieldPanel('content', classname="full"),
    ImageChooserPanel('image'),
    FieldPanel('tags'),
]
