# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='update_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 10, 21, 12, 3, 42, 271257, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
