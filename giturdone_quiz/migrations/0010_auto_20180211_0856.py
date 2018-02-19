# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giturdone_quiz', '0009_answer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='FTQ_Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_text', models.CharField(max_length=600)),
                ('knowledge_mastery', models.IntegerField(default=0)),
                ('black_holes_knowledge', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to=b'post_image', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FTQ_Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.AddField(
            model_name='ftq_answer',
            name='question',
            field=models.ForeignKey(to='giturdone_quiz.FTQ_Question'),
        ),
    ]
