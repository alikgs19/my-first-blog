# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=250)),
                ('commenter', models.ForeignKey(to='blog.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='commnet',
            name='commenter',
        ),
        migrations.RemoveField(
            model_name='commnet',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AlterField(
            model_name='post',
            name='postcontent',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Commnet',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='blog.Post'),
        ),
    ]
