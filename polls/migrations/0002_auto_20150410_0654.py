# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='gameName',
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_data',
            field=models.DateTimeField(verbose_name=b'time'),
        ),
    ]
