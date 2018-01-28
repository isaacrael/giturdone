# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giturdone_quiz', '0003_remove_answer_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='score',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='total_number_correct_answers',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='total_number_wrong_answers',
        ),
    ]
