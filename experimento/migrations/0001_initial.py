# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-22 00:04
from __future__ import unicode_literals

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
                ('fecha_resultado', models.DateTimeField(blank=True, null=True)),
                ('protocolos', models.ManyToManyField(to='protocolo.Protocolo')),
            ],
        ),
    ]
