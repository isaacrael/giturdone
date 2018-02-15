# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giturdone_quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ftq_answer',
            name='knowledge_needs_improvement',
        ),
    ]
