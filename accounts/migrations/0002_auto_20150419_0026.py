# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('balance', models.FloatField()),
            ],
        ),
        migrations.RenameModel(
            old_name='AccountsTypes',
            new_name='AccountsType',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='type',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='user',
        ),
        migrations.DeleteModel(
            name='Accounts',
        ),
        migrations.AddField(
            model_name='account',
            name='type',
            field=models.ForeignKey(to='accounts.AccountsType', to_field=b'type'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
