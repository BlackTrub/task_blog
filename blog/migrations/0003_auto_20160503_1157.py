# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 11:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160502_1533'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'permissions': ('can_view_privatepost', 'Может просматривать приватный пост')},
        ),
    ]
