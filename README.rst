=====
Wagtail Blog
=====

Simple Blog app to plug in to your Wagtail (Django powered CMS) setup/project.

The goal is not to try and become Wordpress or have all its features (or even import/export to it!), but be an extremely simple and powerful blogging app to get your Django/Wagtail blog started.


Quick start
-----------

1. Add `wagtail_blog` to `INSTALLED_APPS`:
  INSTALLED_APPS = {
    ...
    'wagtail_blog'
    ...
  }

2. Configure settings:

  WAGTAIL_BLOG_AUTHOR_PAGE = 'team.TeamMemberPage'  # your wagtail page model with author information

  Optional settings include:

  WAGTAIL_BLOG_POSTS_PER_PAGE = 10  # posts per page on the post listing page

  WAGTAIL_BLOG_FEED_TITLE = 'My Site Feed'  # RSS / Atom feed custom title, defaults to RSS Feed / Atom Feed

  WAGTAIL_BLOG_FEED_DESCRIPTION = 'News Feed of My Site'  # RSS 2.0 / Atom feed custom description, defaults to Blog Post Feed

  WAGTAIL_BLOG_FEED_LENGTH = 50  # How many articles are included in the feed, defaults to 50

3. Templates

The root of your template path should contain blog_page.html and blog_index_page.html files in wagtail_blog catalog.

4. RSS / Atom Feeds

Feeds module of the application contains appropriate feed classes (how to add feed classes into your URL conf - https://docs.djangoproject.com/en/1.7/ref/contrib/syndication/#a-simple-example )
