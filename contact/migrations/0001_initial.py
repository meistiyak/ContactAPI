# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_name', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=20)),
                ('contact_address', models.TextField(max_length=200)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
