from __future__ import absolute_import

from django.utils.functional import cached_property

from wagtail.wagtailadmin.widgets import AdminPageChooser
from wagtail.wagtailcore import blocks

from wagtail_blog.models import BlogPost


class BlogPostSummaryChooserBlock(blocks.PageChooserBlock):
    """
    Displays a summary view of a blog post
    """

    @cached_property
    def target_model(self):
        return BlogPost

    @cached_property
    def widget(self):
        return AdminPageChooser(can_choose_root=False, target_models=[BlogPost])

    class Meta:
        template = 'wagtail_blog/blocks/blog_post_summary.html'
        icon = 'bold'
