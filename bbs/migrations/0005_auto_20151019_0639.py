# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0004_auto_20150925_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bbs',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='bbs_user',
            name='photo',
            field=models.ImageField(default=b'upload_imgs/u=1678328676,1216794096&fm=23&gp=0.jpg', upload_to=b'upload_imgs/'),
        ),
    ]
