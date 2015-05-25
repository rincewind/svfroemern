# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betterimage',
            name='created_at',
            field=models.DateTimeField(verbose_name='Created at', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='betterimage',
            name='height',
            field=models.IntegerField(verbose_name='Height', editable=False),
        ),
        migrations.AlterField(
            model_name='betterimage',
            name='uploaded_by_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Uploaded by user', blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='betterimage',
            name='width',
            field=models.IntegerField(verbose_name='Width', editable=False),
        ),
    ]
