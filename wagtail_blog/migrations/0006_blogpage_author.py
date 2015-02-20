# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20141205_1349'),
        ('blog', '0005_auto_20141210_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='author',
            field=models.ForeignKey(blank=True, to='team.TeamMemberPage', null=True),
            preserve_default=True,
        ),
    ]
