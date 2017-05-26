# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 16:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
        ('experimento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateField(blank=True, default=datetime.datetime.now)),
                ('asistentes', models.ManyToManyField(to='usuario.Usuario')),
                ('cientifico_asignado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cientifico_asignado', to='usuario.Usuario')),
                ('experimentos', models.ManyToManyField(to='experimento.Experimento')),
            ],
        ),
    ]