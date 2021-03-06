# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-29 14:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='frontend.ProductCategory'),
        ),
    ]
