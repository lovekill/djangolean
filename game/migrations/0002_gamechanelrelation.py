# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameChanelRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chanel', models.ForeignKey(to='game.Chanel')),
                ('game', models.ForeignKey(to='game.Game')),
            ],
        ),
    ]
