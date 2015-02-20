# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import modelcluster.fields
import datetime
import wagtail.wagtailcore.fields
from django.conf import settings
import modelcluster.tags


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('wagtailimages', '0004_make_focal_point_key_not_nullable'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
                ('date', models.DateField(verbose_name=b'Post date')),
                ('image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogPageTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', modelcluster.fields.ParentalKey(related_name='tagged_items', to='wagtail_blog.BlogPage')),
                ('tag', models.ForeignKey(related_name='wagtail_blog_blogpagetag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='tags',
            field=modelcluster.tags.ClusterTaggableManager(to='taggit.Tag', through='wagtail_blog.BlogPageTag', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='blogpage',
            old_name='body',
            new_name='content',
        ),
        migrations.AddField(
            model_name='blogpage',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('headline', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='author',
            field=models.ForeignKey(blank=True, to=settings.WAGTAIL_BLOG_AUTHOR_PAGE, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name=b'Post date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateTimeField(default=datetime.date.today, verbose_name=b'Post date'),
            preserve_default=True,
        ),
    ]
