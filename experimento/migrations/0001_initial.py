# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 16:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('protocolo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('resultado', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_resultado', models.DateField(blank=True, default=datetime.datetime.now)),
                ('protocolos', models.ManyToManyField(to='protocolo.Protocolo')),
            ],
        ),
    ]
