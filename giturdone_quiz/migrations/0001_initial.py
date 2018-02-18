# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_text', models.CharField(max_length=200)),
                ('answers', models.IntegerField(default=0)),
                ('correct_answer', models.CharField(default=b'Linus Torvalds', max_length=200)),
                ('total_correct_answers', models.IntegerField(default=0)),
                ('total_wrong_answers', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to=b'post_image', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ftq_Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_text', models.CharField(max_length=1200)),
                ('image', models.ImageField(upload_to=b'post_image', blank=True)),
                ('knowledge_mastery', models.IntegerField(default=0)),
                ('knowledge_needs_improvement', models.IntegerField(default=0)),
                ('knowledge_black_hole', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ftq_Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=400)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='ftq_answer',
            name='question',
            field=models.ForeignKey(to='giturdone_quiz.Ftq_Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='giturdone_quiz.Question'),
        ),
    ]
