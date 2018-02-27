# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giturdone_quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mc_answer',
            name='correct_answer',
            field=models.CharField(default=b'Linus Torvalds', max_length=200),
        ),
        migrations.AddField(
            model_name='mc_answer',
            name='image',
            field=models.ImageField(upload_to=b'post_image', blank=True),
        ),
    ]