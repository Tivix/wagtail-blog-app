from django.conf import settings


def get_blog_author_model():
    if hasattr(settings, 'WAGTAIL_BLOG_AUTHOR_PAGE'):
        return settings.WAGTAIL_BLOG_AUTHOR_PAGE
    else:
        return settings.AUTH_USER_MODEL
