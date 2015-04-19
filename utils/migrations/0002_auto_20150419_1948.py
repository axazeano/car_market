# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150419_0026'),
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(default=b'', null=True, blank=True)),
                ('car_compability', models.ManyToManyField(to='utils.CarsModel')),
            ],
        ),
        migrations.CreateModel(
            name='PartType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(unique=True, max_length=120)),
                ('description', models.TextField(default=b'', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.IntegerField(default=100)),
                ('free', models.IntegerField()),
                ('owner', models.ForeignKey(to='accounts.Account')),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(default=1)),
                ('item', models.ForeignKey(to='utils.Part')),
                ('warehouse', models.ForeignKey(to='utils.Warehouse')),
            ],
        ),
        migrations.AddField(
            model_name='part',
            name='type',
            field=models.ForeignKey(to='utils.PartType'),
        ),
    ]
