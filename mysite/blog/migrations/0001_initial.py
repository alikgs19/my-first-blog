# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commnet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=100)),
                ('postcontent', models.CharField(max_length=500000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('family', models.CharField(max_length=30)),
                ('birthdate', models.DateTimeField(verbose_name=b'birth date')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(to='blog.User'),
        ),
        migrations.AddField(
            model_name='commnet',
            name='commenter',
            field=models.ForeignKey(to='blog.User'),
        ),
        migrations.AddField(
            model_name='commnet',
            name='post',
            field=models.ForeignKey(to='blog.Post'),
        ),
    ]
