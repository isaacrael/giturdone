# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giturdone_quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='total_number_correct_answers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='total_number_wrong_answers',
            field=models.IntegerField(default=0),
        ),
    ]
