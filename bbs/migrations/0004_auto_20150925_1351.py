# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bbs', '0003_auto_20150924_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbs_user',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'upload_imgs/'),
        ),
        migrations.AddField(
            model_name='bbs_user',
            name='signature',
            field=models.CharField(default=b'lazy guy,nothing left', max_length=128),
        ),
        migrations.AddField(
            model_name='bbs_user',
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
