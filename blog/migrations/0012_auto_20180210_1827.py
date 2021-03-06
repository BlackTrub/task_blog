# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-02-10 18:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_userprofile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Profile',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_autor',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_count',
            new_name='count',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_date_create',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_access',
            new_name='is_private',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_date_modify',
            new_name='modified',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_tag',
            new_name='tags',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='tags',
            old_name='tags_name',
            new_name='name',
        ),
    ]
