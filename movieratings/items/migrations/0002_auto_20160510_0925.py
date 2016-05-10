# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 13:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='movie_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='items.Movie'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rater_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='items.Rater'),
        ),
    ]