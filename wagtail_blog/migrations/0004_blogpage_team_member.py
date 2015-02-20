# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20141205_1349'),
        ('blog', '0003_blogindexpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='team_member',
            field=models.ForeignKey(blank=True, to='team.TeamMemberPage', null=True),
            preserve_default=True,
        ),
    ]
