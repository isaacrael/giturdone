# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giturdone_quiz', '0010_auto_20180211_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ftq_answer',
            name='question',
            field=models.ForeignKey(to='giturdone_quiz.Ftq_Question'),
        ),
    ]
