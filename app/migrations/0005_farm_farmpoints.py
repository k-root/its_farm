# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-13 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_wells'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Income', models.IntegerField()),
                ('F_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Farmer')),
            ],
        ),
        migrations.CreateModel(
            name='Farmpoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.IntegerField()),
                ('Lat', models.FloatField()),
                ('Lon', models.FloatField()),
                ('Farm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Farm')),
            ],
        ),
    ]
