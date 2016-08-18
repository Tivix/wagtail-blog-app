# Wagtail Blog

Simple blog app to plug in to your Wagtail (Django powered CMS) project.

The goal is not to try to be Wordpress or have all of its features (or even import/export to it), but rather to be an extremely simple and powerful blogging app to get your Django/Wagtail blog started.

## What's included
Wagtail Blog includes two page types, Blog Index Page (parent) and Blog Post (child), and one Streamfield Block, BlogPostSummaryChooserBlock.

The BlogPostSummaryChooserBlock is a type of PageChooser, and is suitable for manually including a list of relevant Blog Posts on a page.

The pages include basic fields and may be subclassed to add more:

**Blog Index Page**
* Title (inherited from Page, ex. "My Blog")
* Headline (ex. "A Place to Share My Opinions")

**Blog Post**
* Title (inherited from Page)
* Author (ForeignKey relation, see options below)
* Content (RichTextField)
* Image (standard WagtailImage)
* Post Date
* Date Updated
* Tags (standard Wagtail tag implementation)

## Quick start

1. Add `wagtail_blog` to `INSTALLED_APPS`:
    ```
    INSTALLED_APPS = {
    ...
    'wagtail_blog'
    ...
    }
    ```

2. Configure optional settings:

    `WAGTAIL_BLOG_AUTHOR_PAGE = 'settings.AUTH_USER_MODEL'`
    The model to use for blog authors. Defaults to the standard User. You may want to customize this to use something like a TeamMember Wagtail Page model, if you have one.

    `WAGTAIL_BLOG_POSTS_PER_PAGE = 10`
    Posts per page on the post listing page

    `WAGTAIL_BLOG_FEED_TITLE = 'My Site Feed'`
    RSS / Atom feed custom title. Defaults to 'RSS Feed / Atom Feed'

    `WAGTAIL_BLOG_FEED_LINK = '/blog/'`
    The url of your main blog index page for your RSS / Atom feed to link to. Defaults to '/blog/'

    `WAGTAIL_BLOG_FEED_DESCRIPTION = 'News Feed of My Site'`
    RSS 2.0 / Atom feed custom description, defaults to 'Blog Post Feed'

    `WAGTAIL_BLOG_FEED_LENGTH = 50`
    How many articles are included in the feed. Defaults to 50.

3. Templates

    Wagtail Blog includes basic templates for `blog_index_page.html` and `blog_post.html`, as well as fragments for pagination, tags, and related blog posts (via tags). To override these templates with your own, add a `wagtail_blog` directory to the root of your template path. Provided templates follow this structure:
    ```
    wagtail_blog
        blog_index_page.html
        blog_post.html
        blocks
            blog_post_summary.html
        fragments
            paginator.html
            related.html
            tags.html
    ```
4. RSS / Atom Feeds

    Feeds module of the application contains appropriate feed classes. [How to add feed classes into your URL conf](https://docs.djangoproject.com/en/1.7/ref/contrib/syndication/#a-simple-example )
