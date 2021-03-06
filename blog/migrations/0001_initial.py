# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 17:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=100)),
                ('article_text', models.TextField()),
                ('article_date_create', models.DateTimeField(default=django.utils.timezone.now)),
                ('article_date_modify', models.DateTimeField(default=django.utils.timezone.now)),
                ('article_access', models.BooleanField(default=True)),
                ('article_autor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='article_tag',
            field=models.ManyToManyField(to='blog.Tags'),
        ),
    ]
