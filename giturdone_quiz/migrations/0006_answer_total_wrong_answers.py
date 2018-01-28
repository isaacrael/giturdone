# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giturdone_quiz', '0005_answer_total_correct_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='total_wrong_answers',
            field=models.IntegerField(default=0),
        ),
    ]
