from django.utils.html import format_html, format_html_join
from django.conf import settings

from wagtail.wagtailcore import hooks
from wagtail.wagtailcore.whitelist import allow_without_attributes, attribute_rule


@hooks.register('construct_whitelister_element_rules')
def whitelister_element_rules():
    return {
        'blockquote': allow_without_attributes,
        'code': allow_without_attributes,
        'table': allow_without_attributes,
        'tr': allow_without_attributes,
        'td': allow_without_attributes,
        'pre': attribute_rule({'class': True}),
    }


@hooks.register('insert_editor_js')
def editor_js():
    js_files = [
        'global/js/hallo-code-snippet.js',
        'global/js/hallo-code-block.js',
        'global/js/hallo-tables.js',
        'global/js/hallo-quote-snippet.js',
        'global/js/hallo-htmledit.js',
    ]

    js_includes = format_html_join(
        '\n',
        '<script src="{0}{1}"></script>',
        ((settings.STATIC_URL, filename) for filename in js_files)
    )

    return js_includes + format_html(
        """
        <script>
            registerHalloPlugin('codesnippet');
            registerHalloPlugin('codeblock');
            registerHalloPlugin('tables');
            registerHalloPlugin('quotesnippet');
            registerHalloPlugin('editHtmlButton');
        </script>
        """
    )


@hooks.register('insert_editor_css')
def editor_css():
    css_files = [
        'global/font-awesome/css/font-awesome.css',
        'global/css/wagtail-admin.css',
    ]

    css_includes = format_html_join(
        '\n',
        '<link rel="stylesheet" href="{0}{1}">',
        ((settings.STATIC_URL, filename) for filename in css_files)
    )

    return css_includes
