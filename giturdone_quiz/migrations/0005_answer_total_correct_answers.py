# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giturdone_quiz', '0004_auto_20180127_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='total_correct_answers',
            field=models.IntegerField(default=0),
        ),
    ]
