# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giturdone_quiz', '0008_auto_20180129_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='image',
            field=models.ImageField(upload_to=b'post_image', blank=True),
        ),
    ]
