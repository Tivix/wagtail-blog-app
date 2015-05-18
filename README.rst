=====
Wagtail Blog
=====

Simple Blog app to plug in to your Wagtail setup.

Quick start
-----------

1. Add "wagtail_blog" to INSTALLED_APPS:
  INSTALLED_APPS = {
    ...
    'wagtail_blog'
  }

2. Configure required settings:

  WAGTAIL_BLOG_AUTHOR_PAGE = 'team.TeamMemberPage'  # your wagtail page model with author information

  WAGTAIL_BLOG_POSTS_PER_PAGE = 10  # posts per page on the post listing page

  Optional settings include:

  WAGTAIL_BLOG_FEED_TITLE = 'My Site Feed'  # RSS / Atom feed custom title

  WAGTAIL_BLOG_FEED_DESCRIPTION = 'News Feed of My Site'  # RSS / Atom feed custom description

3. Templates

The root of your template path should contain blog_page.html and blog_index_page.html files in wagtail_blog catalog.

4. RSS / Atom Feeds

Feeds module of the application contains appropriate feed classes (how to add feed classes into your URL conf - https://docs.djangoproject.com/en/1.7/ref/contrib/syndication/#a-simple-example )
