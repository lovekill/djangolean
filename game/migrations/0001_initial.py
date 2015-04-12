# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chanel',
            fields=[
                ('chanel_id', models.AutoField(primary_key=True, serialize=False)),
                ('chanel_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_id', models.AutoField(primary_key=True, serialize=False)),
                ('game_name', models.CharField(max_length=50)),
                ('create_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('imei', models.CharField(max_length=64)),
                ('imsi', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='chanel',
            name='game',
            field=models.ManyToManyField(to='game.Game'),
        ),
    ]
