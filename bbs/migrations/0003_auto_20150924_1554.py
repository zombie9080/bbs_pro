# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0002_auto_20150924_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='BBS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64)),
                ('summary', models.CharField(max_length=256, null=True, blank=True)),
                ('content', models.TextField()),
                ('view_count', models.IntegerField()),
                ('ranking', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='BBS_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='bbs',
            name='author',
            field=models.ForeignKey(to='bbs.BBS_user'),
        ),
    ]
