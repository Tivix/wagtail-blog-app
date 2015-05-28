from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager

from taggit.models import TaggedItemBase
from datetime import date, datetime


# This model is enough so that the HomePage model can
# include a page chooser for the featured blog post
class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage', related_name='tagged_items')


class BlogPage(Page):
    content = RichTextField()
    author = models.ForeignKey(
        settings.WAGTAIL_BLOG_AUTHOR_PAGE, blank=True, null=True)

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    date = models.DateTimeField("Post date", default=date.today)
    date_updated = models.DateTimeField(default=datetime.now)

    @property
    def blog_index(self):
        return self.get_ancestors().type(BlogIndexPage).last()

    def get_absolute_url(self):
        return self.full_url


class BlogIndexPage(Page):
    subpage_types = ['BlogPage']
    headline = models.CharField(max_length=255, blank=True, null=True)

    @property
    def blogs(self):
        blogs = BlogPage.objects.live().descendant_of(self)
        blogs = blogs.order_by('-date')
        return blogs

    def get_context(self, request):

        blogs = self.blogs

        tag = request.GET.get('tag')
        if tag:
            blogs = blogs.filter(tags__name=tag)

        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(blogs,
            getattr(settings, 'WAGTAIL_BLOG_POSTS_PER_PAGE', 10))

        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        context = super(BlogIndexPage, self).get_context(request)
        context['blogs'] = blogs
        return context
