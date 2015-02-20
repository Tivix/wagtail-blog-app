=====
Wagtail Blog
=====

Simple Blog app to plugin into your wagtail setup.

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

3. Templates

The root of your template path should contain blog_page.html and blog_index_page.html files in wagtail_blog catalog.
