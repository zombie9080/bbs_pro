# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bbs',
            name='author',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='BBS',
        ),
        migrations.DeleteModel(
            name='BBS_user',
        ),
    ]
