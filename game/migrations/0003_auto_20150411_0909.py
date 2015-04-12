# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_gamechanelrelation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chanel',
            name='game',
        ),
        migrations.AddField(
            model_name='game',
            name='chanel',
            field=models.ManyToManyField(to='game.Chanel'),
        ),
    ]
