# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giturdone_quiz', '0002_remove_ftq_answer_knowledge_needs_improvement'),
    ]

    operations = [
        migrations.AddField(
            model_name='ftq_answer',
            name='knowledge_needs_improvement',
            field=models.IntegerField(default=0),
        ),
    ]
