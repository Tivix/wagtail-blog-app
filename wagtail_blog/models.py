from datetime import date, datetime

from django.db import models
from django.db.models import Count
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404

from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.url_routing import RouteResult

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import Tag, TaggedItemBase


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

    @property
    def related_blogs(self):
        # Get all tags associated with this post
        tags = self.tags.all()

        # Get objects which share tags, count the number they share
        matches = BlogPage.objects.filter(tags__in=tags).annotate(Count('title'))
        matches = matches.exclude(pk=self.pk)

        # Return up to 5 results
        related = matches.order_by('-title__count')[:5]

        return related


class BlogIndexPage(Page):
    subpage_types = ['BlogPage']
    headline = models.CharField(max_length=255, blank=True, null=True)


    def route(self, request, path_components):

        if path_components:
            """
            Customized to correctly route legacy blog posts with too long slugs.
            Additionally customized handle tags url
            """
            if path_components[0] == 'tags':
                # If first component is "tags", we handle that tag
                # URL for tags is /blog/tags/tag_name
                tag_slug = path_components[1]

                # Check if Tag with given name exists, if not raise 404.
                try:
                    tag = Tag.objects.get(slug__iexact=tag_slug)
                except Tag.DoesNotExist:
                    raise Http404

                if self.live:
                    return RouteResult(self, kwargs={"tag": tag})

                # if not components nor it's live
                raise Http404

            else:
                # If the first component is not "tags", handle legacy blog slug
                # Legacy blog posts have slugs with max_length=255 so we need
                # to make them compatible with new Wagtail's 50 chars limit.
                path_components[0] = path_components[0][:50]

        return super(BlogIndexPage, self).route(request, path_components)

    @property
    def blogs(self):
        blogs = BlogPage.objects.live().descendant_of(self)
        blogs = blogs.order_by('-date')
        return blogs

    def get_context(self, request, tag=None):
        blogs = self.blogs

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
