# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpage',
            old_name='body',
            new_name='content',
        ),
        migrations.AddField(
            model_name='blogpage',
            name='author',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpage',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 4, 8, 5, 17, 842170)),
            preserve_default=False,
        ),
    ]
